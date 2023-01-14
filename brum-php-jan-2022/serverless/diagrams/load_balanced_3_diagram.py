from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, ElasticLoadBalancing
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.database import Elasticache, RDS

import os

base_dir = os.path.dirname(__file__)

def build_server(instance_number):
    with Cluster(f"EC2 instance {instance_number}\n(t3.large, dual core, 4gb ram)"):
        nginx = Custom("Nginx", f'img/nginx.png')
        phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
        nginx >> Edge(style="dashed") << phpfpm
    return nginx
                

with Diagram("AWS Load balancer. Quintuple Server", filename=f"{base_dir}/load_balanced_3_diagram", show=False):
    with Cluster("AWS Region"):
        load_balancer = ElasticLoadBalancing("Load Balancer")

        with Cluster("Auto Scaling Group"):
           cluster = [build_server(i + 1) for i in range(5)]
                
        
        load_balancer >> Edge() << cluster
            