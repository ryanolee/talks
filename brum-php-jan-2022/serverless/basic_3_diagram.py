# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals With Database", filename=f"{base_dir}/basic_3_diagram", show=False):
    with Cluster("Server\n(dual core, 4GB of ram)"):
        nginx = Custom("Nginx", f'img/nginx.png')
        phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
        mysql = Custom("MySQL\n(Database)", f'img/mysql.png')
        nginx >> Edge(style="dashed") << phpfpm
        phpfpm >> Edge(style="dashed") << mysql
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << nginx