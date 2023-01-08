from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, ElasticLoadBalancing
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.database import Elasticache, RDS

import os

base_dir = os.path.dirname(__file__)
with Diagram("Distributed Example with AWS Services + Autoscaling", filename=f"{base_dir}/load_balanced_1_diagram", show=False):
    with Cluster("AWS Region"):
        load_balancer = ElasticLoadBalancing("Load Balancer")

        with Cluster("Auto Scaling Group"):
            with Cluster("EC2 instance 1\n(t3.large, dual core, 4gb ram)"):
                nginx_1 = Custom("Nginx", f'img/nginx.png')
                phpfpm_1 = Custom("PhpFpm", f'img/phpfpm.png')
                nginx_1 >> Edge(style="dashed") << phpfpm_1
            
            with Cluster("EC2 instance 2\n(t3.large, dual core, 4gb ram)"):
                nginx_2 = Custom("Nginx", f'img/nginx.png')
                phpfpm_2 = Custom("PhpFpm", f'img/phpfpm.png')
                nginx_2 >> Edge(style="dashed") << phpfpm_2
        
        load_balancer >> Edge() << [nginx_1, nginx_2]
            