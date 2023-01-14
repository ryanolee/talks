import plotly.graph_objects as go
import random 
import os

base_dir = os.path.dirname(__file__)

date_times_by_minute = [f'2022-01-19 19:{i}:00' for i in range(0, 60)]
requests_per_second = [
   # Traffic jumps between 2 and 5 requests per second for an hour
    *[random.randint(1,4) for i in range(0, 60)],
]


fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=date_times_by_minute, y=requests_per_second, name='Average Requests per Second',
                         line=dict(color='royalblue', width=4, dash='dot')))
fig.update_yaxes(anchor="x", range=[0, 60], title_text="Requests per Second")
fig.update_xaxes(title_text="Time")
fig.write_image(f"{base_dir}/lesser_used_traffic_chart.png")