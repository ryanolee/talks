# diagram.py
from diagrams import Diagram, Edge
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server", show=False):
    Custom("Client", f'{base_dir}/img/client.png') >> Edge() << Custom("Server", f'{base_dir}/img/server.png')