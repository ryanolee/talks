from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.compute import Lambda
from diagrams.aws.management import Cloudformation
import os

base_dir = os.path.dirname(__file__)

base_dir = os.path.dirname(__file__)
with Diagram("Relationships", filename=f"{base_dir}/bref_relationship_1_diagram", show=False):
    
    with Cluster("AWS Services"):
        aws_lambda = Lambda("AWS Lambda")
        aws_cloudformation = Cloudformation("AWS CloudFormation")
        
        

    serverless = Custom("Serverless Framework", f'img/serverless.png')
    bref = Custom("Bref PHP", f'img/brefphp.jpg')
    php = Custom("PHP", f'img/elephpantblue_1_.png')

    aws_cloudformation >> Edge(label="Deploys") >> aws_lambda
    bref >> Edge(label="Provides Runtime For") >> aws_lambda
    bref >> Edge(label="Is Plugin of") >> serverless
    serverless >> Edge(label="Generates") >> aws_cloudformation
    aws_lambda >> Edge(label="Runs") >> php