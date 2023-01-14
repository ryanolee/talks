# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals with Database + Redis + Elastic", filename=f"{base_dir}/basic_5_diagram", show=False):
    with Cluster("Server\n(quad core, 12GB of ram)"):
        nginx = Custom("Nginx", f'img/nginx.png')
        phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
        mysql = Custom("MySQL\n(Database)", f'img/mysql.png')
        redis = Custom("Redis\n(In Memory Cache)", f'img/redis.png')
        elastic = Custom("Elastic Search\n(Indexable Search Engine)", f'img/elasticsearch.png')
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge(style="dashed") << [mysql, redis, elastic]
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << nginx