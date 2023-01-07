# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals ... 4 years later", filename=f"{base_dir}/basic_8_diagram", show=False):
    with Cluster("Server\n(Do not touch)\n(eight core, 32GB of ram)"):
        magic = Custom("Magic!", f'img/magic.jpeg')
    
    Custom("Client", f'img/client.png') >> Edge(label="HTTP/HTTPs") << magic