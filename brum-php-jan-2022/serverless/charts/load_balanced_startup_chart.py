import plotly.express as px
import pandas as pd
import os

base_dir = os.path.dirname(__file__)

df = pd.DataFrame([
    dict(Process="CPU Load Above Average for 5 minutes", Start='2022-01-19 19:30:00', Finish='2022-01-19 19:35:00'),
    dict(Process="Provision New Server", Start='2022-01-19 19:35:00', Finish='2022-01-19 19:36:30'),
    dict(Process="Start Services", Start='2022-01-19 19:36:30', Finish='2022-01-19 19:37:00'),
    dict(Process="Add Server to Load Balancer", Start='2022-01-19 19:37:00', Finish='2022-01-19 19:37:30'),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Process", height=300)
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.write_image(f"{base_dir}/load_balanced_startup_chart.png")