import plotly.graph_objects as go
import random 
import os

base_dir = os.path.dirname(__file__)

date_times_by_minute = [f'2022-01-19 19:{i}:00' for i in range(0, 60)]
requests_per_second = [
    #Stable for first 20 minutes
    *[random.randint(6, 13) for i in range(0, 20)],
    # Then a spike
    *[17, 18, 25, 28 , 22, 29, 35, 38, 41, 50],
    # stable for the next 10 minutes at 50 Requests per second + or - 5
    *[random.randint(45, 55) for i in range(0, 10)],
    # Then a ramp down to original levels over 10 minutes
    *[50, 44, 38, 32, 26, 20, 14, 15, 18, 19],
    # Then stability for the last 10 minutes
    *[random.randint(6, 13) for i in range(0, 10)],
]



server_size = 5
sample_rate = 2
server_count = 10
restrict_to_one_by_one = True

total_servers = []
date_times_by_n_minute = [f'2022-01-19 19:{i}:00' for i in range(0, 60, sample_rate)]
for i in range(0, 60, sample_rate):
    requests_per_second_average = sum(requests_per_second[i:i+sample_rate]) / sample_rate
    rounded_average = round(requests_per_second_average / server_size) * server_size
    
    if not restrict_to_one_by_one:
        total_servers.append(rounded_average)
        continue

    if rounded_average > server_count:
        server_count += server_size
    elif rounded_average < server_count:
        server_count -= server_size
    total_servers.append(server_count)

fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=date_times_by_minute, y=requests_per_second, name='Average Requests per Second',
                         line=dict(color='royalblue', width=4, dash='dot')))

fig.add_bar(x=date_times_by_n_minute, y=total_servers, name='Requests per Second\nCluster can handle', marker_color='indianred')
fig.write_image(f"{base_dir}/load_balanced_over_time_2_chart.png")