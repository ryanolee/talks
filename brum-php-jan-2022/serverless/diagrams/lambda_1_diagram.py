from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, ElasticLoadBalancing
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.database import Elasticache, RDS
from diagrams.aws.compute import Lambda

import os

base_dir = os.path.dirname(__file__)
with Diagram("Aws Lambda Instead?", filename=f"{base_dir}/lambda_1_diagram", show=False):
    with Cluster("AWS Region"):

        load_balancer = ElasticLoadBalancing("Load Balancer")

        with Cluster("Lambda Target Group"):
            aws_lambda = Lambda("Lambda")
            
            
            
        mysql = RDS("RDS\n(MySql Database)")
        elasticache = Elasticache("Elastic Cache Cluster\n(Redis)")
        elastic = ElasticsearchService("Elastic Search Service")
        cloudfront = CloudFront("Cloudfront\n(CDN)")
        bucket = S3("S3 Bucket\n(Image / Media storage)")
        
        cloudfront >> Edge() << load_balancer
        cloudfront >> Edge() << bucket
        aws_lambda >> Edge() << load_balancer
        aws_lambda >> Edge() << [mysql, elasticache, elastic]
        
        

    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << cloudfront