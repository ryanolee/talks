# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals", show=True):
    with Cluster("Server\n(dual core, 4GB of ram)"):
        nginx = Custom("Nginx", f'{base_dir}/img/nginx.png')
        phpfpm = Custom("PhpFpm", f'{base_dir}/img/phpfpm.png')
        nginx >> Edge(style="dashed") << phpfpm
    
    Custom("Client", f'{base_dir}/img/client.png') >> Edge(label="HTTP/HTTPs") << nginx