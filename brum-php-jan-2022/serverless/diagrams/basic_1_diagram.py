# diagram.py
from diagrams import Diagram, Edge
from diagrams.custom import Custom
import os

base_dir = os.path.dirname(__file__)
with Diagram("Client Server", filename=f"{base_dir}/basic_1_diagram", show=False):
    Custom("Client", f'img/client.png') >> Edge() << Custom("Server", f'img/server.png')