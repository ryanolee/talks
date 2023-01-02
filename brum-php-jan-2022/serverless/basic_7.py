# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals with Lots of stuff + who knows what!?", show=True):
    with Cluster("Server\n(eight core, 32GB of ram)"):
        nginx = Custom("Nginx", f'{base_dir}/img/nginx.png')
        phpfpm = Custom("PhpFpm", f'{base_dir}/img/phpfpm.png')
        phpcron = Custom("Php Cron Jobs", f'{base_dir}/img/phpcli.png')
        mysql = Custom("MySQL\n(Database)", f'{base_dir}/img/mysql.png')
        redis = Custom("Redis\n(In Memory Cache)", f'{base_dir}/img/redis.png')
        elastic = Custom("Elastic Search\n(Indexable Search Engine)", f'{base_dir}/img/elasticsearch.png')
        varnish = Custom("Varnish\n(HTTP Reverse Cache Proxy)", f'{base_dir}/img/varnish.png')
        varnish >> Edge(style="dashed") << nginx
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge(style="dashed") << [mysql, redis, elastic]
        phpcron >> Edge(style="dashed") << [mysql, redis, elastic]
    
    Custom("Client", f'{base_dir}/img/client.png') >> Edge(label="HTTP/HTTPs") << varnish