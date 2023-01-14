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
    [100, 850 ],
    width,
    ["#018e37", "#787cb5"]
)

# 5 Servers stacked on top of each other 
ax.bar("Total", 200, width, bottom=0, label="Server 1", color="#7a79f1")
ax.bar("Total", 200, width, bottom=200, label="Server 2", color="#db657e")
ax.bar("Total", 200, width, bottom=400, label="Server 3", color="#38fa6e")
ax.bar("Total", 200, width, bottom=600, label="Server 4", color="#bf4390")
ax.bar("Total", 200, width, bottom=800, label="Server 5", color="#8210d8")





ax.set_ylabel('Percentage')
ax.set_title('Server CPU Usage')
ax.legend()

plt.savefig(f'{base_dir}/load_balanced_3_chart.png')
