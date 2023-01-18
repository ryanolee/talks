from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.database import DynamodbTable
from diagrams.aws.storage import S3
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)

with Diagram("Relationships", filename=f"{base_dir}/bref_building_something_6_diagram", show=False):
    with Cluster("Internet"):
        client = Custom("Client", f'img/client.png')
        developer = Custom("Developer", f'img/developer.png')

    with Cluster("AWS eu-west-1"):
        with Cluster("Bref PHP \"Web App\" Layer"):
            aws_frontend_lambda = Lambda("AWS Frontend\nLambda")

        with Cluster("Bref PHP \"Console\" Layer"): 
            aws_console_lambda = Lambda("Console\n Lambda")
        
        with Cluster("Bref PHP \"Event\" Layer"): 
            aws_event_lambda = Lambda("Console\n Lambda")

        aws_api_gw = APIGateway("API Gateway")
        aws_dynamodb = DynamodbTable("DynamoDb Table")
        aws_cloudfront = CloudFront("CloudFront CDN")
        aws_static_asset_bucket = S3("Static Assets\nBucket")
        aws_image_bucket = S3("Image Bucket") 
    
    client >> Edge(label="Viewing Images / Presigned POST Upload") << aws_image_bucket 
    developer >> Edge(label="Bref CLI Console Invoke") << aws_console_lambda
    client >> Edge(label="HTTP Requests") << aws_cloudfront
    aws_cloudfront >> Edge(label="/*") << aws_api_gw
    aws_cloudfront >> Edge(label="/assets/*") << aws_static_asset_bucket
    [aws_frontend_lambda, aws_console_lambda] >> Edge(label="Query") << aws_dynamodb
    aws_api_gw >> Edge(label="Fast CGI") << aws_frontend_lambda
    aws_image_bucket >> Edge(label="S3 Image Upload Event") >> aws_event_lambda
    aws_event_lambda >> Edge(label="Write Image URL") >> aws_dynamodb

