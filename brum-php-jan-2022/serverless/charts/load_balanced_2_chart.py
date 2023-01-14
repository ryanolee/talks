import matplotlib.pyplot as plt
import os
base_dir = os.path.dirname(__file__)
labels = ['Server CPU Usage']
width = 0.35 

fig, ax = plt.subplots()

def render_stacked(ax, labels, data, width, colors):
    bottom = 0
    for i, d in enumerate(data):
        ax.bar("Load", d, width, bottom=bottom,
               label=labels[i], color=colors[i])
        bottom += d

render_stacked(ax,
    ["Nginx", "PhpFpm"],
    [20, 150 ],
    width,
    ["#018e37", "#787cb5"]
)

ax.bar("Total", 200, width, bottom=0, label="Server 1", color="#FFA500")


ax.set_ylabel('Percentage')
ax.set_title('Server CPU Usage')
ax.legend()

plt.savefig(f'{base_dir}/load_balanced_2_chart.png')
