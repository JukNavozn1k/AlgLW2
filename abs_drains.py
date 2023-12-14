import networkx as nx
import matplotlib.pyplot as plt

# Define your graph (replace this with your graph initialization)
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Function to find absolute drains
def absolute_drains(graph):
    drains = []
    for node in graph.nodes():
        if nx.is_strongly_connected(graph.subgraph(nx.descendants(graph, node) | {node})):
            drains.append(node)
    return drains

absolute_drains_count = len(absolute_drains(G))


plt.figure(figsize=(8, 6))
plt.title(f"Количество абсолютных стоков: {absolute_drains_count}", fontsize=16, color='blue')
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12)

plt.show()
