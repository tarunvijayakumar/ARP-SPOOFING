import tkinter as tk
from networkx import Graph
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_network_graph(mac_ip_map):
    G = Graph()
    for ip, mac in mac_ip_map.items():
        G.add_edge(ip, mac)
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, with_labels=True, ax=ax)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.title("Advanced ARPGuard Dashboard")
tk.Label(window, text="Real-Time Network Visualization").pack()
tk.Button(window, text="Show Network Graph", command=lambda: show_network_graph(mac_ip_map)).pack()
window.mainloop()
