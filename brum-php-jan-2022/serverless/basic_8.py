# diagram.py
from diagrams import Diagram, Edge, Cluster
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server Internals ... 4 years later", show=True):
    with Cluster("Server\n(Do not touch)\n(eight core, 32GB of ram)"):
        magic = Custom("Magic!", f'{base_dir}/img/magic.jpeg')
    
    Custom("Client", f'{base_dir}/img/client.png') >> Edge(label="HTTP/HTTPs") << magic