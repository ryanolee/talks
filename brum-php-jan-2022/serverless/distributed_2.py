from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.database import Elasticache, RDS

import os

base_dir = os.path.dirname(__file__)
with Diagram("Distributed Example with AWS Services", show=True):
    with Cluster("AWS Region"):
        with Cluster("EC2 instance\n(t3.xlarge, quad core, 16GB of ram)"):
            nginx = Custom("Nginx", f'{base_dir}/img/nginx.png')
            phpfpm = Custom("PhpFpm", f'{base_dir}/img/phpfpm.png')
            phpcron = Custom("Php Cron Jobs", f'{base_dir}/img/phpcli.png')

        mysql = RDS("RDS\n(MySql Database)")
        elasticache = Elasticache("Elastic Cache Cluster\n(Redis)")
        elastic = ElasticsearchService("Elastic Search Service")
        cloudfront = CloudFront("Cloudfront\n(CDN)")
        bucket = S3("S3 Bucket\n(Image / Media storage)")
        
        cloudfront >> Edge() << nginx
        cloudfront >> Edge() << bucket
        phpfpm >> bucket
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge() << [mysql, elasticache, elastic]
    
    Custom("Client", f'{base_dir}/img/client.png') >> Edge(label="HTTP/HTTPs") << cloudfront