import tkinter as tk
from networkx import Graph
import networkx as nx
import matplotlib.pyplot as plt

def show_network_graph(mac_ip_map):
    G = Graph()
    for ip, mac in mac_ip_map.items():
        G.add_edge(ip, mac)
    nx.draw(G, with_labels=True)
    plt.show()

def main():
    window = tk.Tk()
    window.title("ARPGuard Dashboard")
    tk.Label(window, text="ARP Alert Dashboard").pack()
    tk.Button(window, text="Show Network Graph", command=lambda: show_network_graph(mac_ip_map)).pack()
    window.mainloop()

if __name__ == "__main__":
    mac_ip_map = {'192.168.1.2': 'aa:bb:cc:dd:ee:ff', '192.168.1.3': 'ab:cd:ef:12:34:56'} # Replace with live data
    main()
