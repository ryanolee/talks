from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.database import DynamodbTable
from diagrams.aws.storage import S3
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)

with Diagram("Relationships", filename=f"{base_dir}/bref_building_something_1_diagram", show=False):
    client = Custom("Client", f'img/client.png')
    with Cluster("AWS eu-west-1"):
        with Cluster("Bref PHP \"Web App\""):
            aws_frontend_lambda = Lambda("AWS Frontend\nLambda")
     
        aws_api_gw = APIGateway("API Gateway")
    
    client >> Edge(label="HTTPs Requests") << aws_api_gw
    aws_api_gw >> Edge(label="Fast CGI") << aws_frontend_lambda

