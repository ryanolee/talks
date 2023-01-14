
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront, ElasticLoadBalancing
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.database import Elasticache, RDS
from diagrams.aws.compute import Lambda
from diagrams.aws.management import CloudwatchEventTimeBased
from diagrams.aws.mobile import APIGateway
import os

base_dir = os.path.dirname(__file__)
with Diagram("Distributed Example with AWS Services + Lambda", filename=f"{base_dir}/lambda_2_diagram", show=False):
    with Cluster("AWS Region"):
        with Cluster("Data Layer"):
            mysql = RDS("RDS\n(MySql Database)")
            elasticache = Elasticache("Elastic Cache Cluster\n(Redis)")
            elastic = ElasticsearchService("Elastic Search Service")
            bucket = S3("S3 Bucket\n(Image / Media storage)")

        with Cluster("App Layer"):
            
            with Cluster("Main Web Server"):
                cloudfront = CloudFront("Cloudfront\n(CDN)")
                load_balancer = ElasticLoadBalancing("Load Balancer")

                with Cluster("Auto Scaling Group"):
                    with Cluster("EC2 instance 1\n(t3.large, dual core, 4gb ram)"):
                        nginx_1 = Custom("Nginx", f'img/nginx.png')
                        phpfpm_1 = Custom("PhpFpm", f'img/phpfpm.png')
                        nginx_1 >> Edge(style="dashed") << phpfpm_1

            with Cluster("Cron Job(s)"):
                aws_cron_lambda = Lambda("Cron Job\n(Report Generation)")
                aws_cron_event = CloudwatchEventTimeBased("Run every Hour\n(Report Generation)") 
                aws_cron_event >> aws_cron_lambda >> Edge() << mysql
            
            with Cluster("APIs"):
                api_gw = APIGateway("API Gateway")
                aws_lambda_payment = Lambda("Lambda\n(Payment API)")
                aws_lambda_reporting = Lambda("Lambda\n(Reporting  API)")
                api_gw >> Edge() << [aws_lambda_payment, aws_lambda_reporting]
                aws_lambda_payment >> Edge() << mysql
                aws_lambda_reporting >> Edge() << mysql
        
        

        cloudfront >> Edge() << load_balancer
        load_balancer >> Edge() << [nginx_1]
        cloudfront >> Edge() << bucket
        phpfpm_1 >> bucket
        phpfpm_1 >> Edge() << [mysql, elasticache, elastic]

        
        
    Custom("Some External Service", f'img/cloud.png') >> Edge() << aws_cron_lambda
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << [cloudfront, api_gw]
    