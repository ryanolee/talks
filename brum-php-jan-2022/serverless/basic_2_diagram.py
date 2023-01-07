# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals", filename=f"{base_dir}/basic_2_diagram", show=False):
    with Cluster("Server\n(dual core, 4GB of ram)"):
        nginx = Custom("Nginx", f'img/nginx.png')
        phpfpm = Custom("PhpFpm", f'img/phpfpm.png')
        nginx >> Edge(style="dashed") << phpfpm
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << nginx