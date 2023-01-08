from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals Distributed", filename=f"{base_dir}/distributed_1_diagram", show=False):
    with Cluster("Our Data Center / AWS / Azure / ect.."):
        with Cluster("App Server\n(quad core, 16GB of ram)"):
            nginx = Custom("Nginx", f'img/nginx.png')
            phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
            phpcron = Custom("Php Cron Jobs", f'img/phpcli.png')
        
        with Cluster("Database Server\n(dual core 4 GB of ram)"):
            mysql = Custom("MySQL\n(Database)", f'img/mysql.png')
    
        with Cluster("Redis Server\n(single core) 2GB of ram"):
            redis = Custom("Redis\n(In Memory Cache)", f'img/redis.png')

        with Cluster("Elastic search server\n(single core) 2GB of ram"):
            elastic = Custom("Elastic Search\n(Indexable Search Engine)", f'img/elasticsearch.png')
        
        with Cluster("Varnish server\n(single core, 4GB of ram)"):
            varnish = Custom("Varnish\n(HTTP Reverse Cache Proxy)", f'img/varnish.png')
        
        varnish >> Edge() << nginx
        nginx >> Edge() << phpfpm
        phpfpm >> Edge() << [mysql, redis, elastic]
        phpcron >> Edge() << [mysql, redis, elastic]
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << varnish