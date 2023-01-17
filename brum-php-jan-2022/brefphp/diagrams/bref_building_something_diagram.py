from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.database import DynamodbTable
from diagrams.aws.storage import S3
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)

with Diagram("Relationships", filename=f"{base_dir}/bref_building_something_diagram", show=False):
    client = Custom("Client", f'img/client.png')
    with Cluster("AWS eu-west-1"):
        with Cluster("Bref PHP \"Web App\""):
            aws_frontend_lambda = Lambda("AWS Frontend\nLambda")
        with Cluster("Bref PHP \"Lambda Event\""): 
            aws_processing_lambda = Lambda("Image Processing\n Lambda")
        aws_api_gw = APIGateway("API Gateway")
        aws_dynamodb = DynamodbTable("Phpelephant Images\nDynamoDb Table")
        aws_s3_images = S3("Phpelephant\nImages Bucket")
    

    client >> Edge(label="Load web pages") << aws_api_gw
    client << Edge(label="Get Presigned URL") << aws_api_gw
    client >> Edge(label="Upload Image Using S3 Presigned Url") >> aws_s3_images
    aws_frontend_lambda >> Edge(label="Query and create image record") << aws_dynamodb
    aws_processing_lambda >> Edge(label="Update Image Record") << aws_dynamodb
    aws_api_gw >> Edge(label="Lambda Proxy") << aws_frontend_lambda
    aws_s3_images >> Edge(label="S3 Event triggers lambda") >> aws_processing_lambda
    aws_s3_images << Edge(label="Newly processed image written back to bucket") << aws_processing_lambda

