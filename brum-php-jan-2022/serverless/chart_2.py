import matplotlib.pyplot as plt
import os
base_dir = os.path.dirname(__file__)
labels = ['Server CPU Usage']
width = 0.35 

fig, ax = plt.subplots()

def render_stacked(ax, labels, data, width, colors):
    bottom = 0
    for i, d in enumerate(data):
        ax.bar("Current server", d, width, bottom=bottom,
               label=labels[i], color=colors[i])
        bottom += d

render_stacked(ax,
    ["Redis", "Varnish", "Nginx", "PhpFpm", "PhpCron", "MySQL", "ElasticSearch"],
    [50, 60, 20, 420, 20, 100, 50],
    width,
    ["#e32820", "#575756", "#018e37", "#787cb5", "#b0b36d", "#e68a10", "#3bb4a7"]
)

ax.bar("Total", 800, width, bottom=0, label="Total", color="#7a79f1")

ax.set_ylabel('Percentage')
ax.set_title('Server CPU Usage')
ax.legend()

plt.savefig(f'{base_dir}/chart_2.png')
