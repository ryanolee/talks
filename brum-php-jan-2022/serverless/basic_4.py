# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals with Database + Redis", show=True):
    with Cluster("Server\n(dual core, 6GB of ram)"):
        nginx = Custom("Nginx", f'{base_dir}/img/nginx.png')
        phpfpm = Custom("PhpFpm", f'{base_dir}/img/phpfpm.png')
        mysql = Custom("MySQL\n(Database)", f'{base_dir}/img/mysql.png')
        redis = Custom("Redis\n(In Memory Cache)", f'{base_dir}/img/redis.png')
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge(style="dashed") << [mysql, redis]
    
    Custom("Client", f'{base_dir}/img/client.png') >> Edge(label="HTTP/HTTPs") << nginx