# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals with Lots of stuff + who knows what!?", filename=f"{base_dir}/basic_7_diagram", show=False):
    with Cluster("Server\n(eight core, 32GB of ram)"):
        nginx = Custom("Nginx", f'img/nginx.png')
        phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
        phpcron = Custom("Php Cron Jobs", f'img/phpcli.png')
        mysql = Custom("MySQL\n(Database)", f'img/mysql.png')
        redis = Custom("Redis\n(In Memory Cache)", f'img/redis.png')
        elastic = Custom("Elastic Search\n(Indexable Search Engine)", f'img/elasticsearch.png')
        varnish = Custom("Varnish\n(HTTP Reverse Cache Proxy)", f'img/varnish.png')
        varnish >> Edge(style="dashed") << nginx
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge(style="dashed") << [mysql, redis, elastic]
        phpcron >> Edge(style="dashed") << [mysql, redis, elastic]
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << varnish