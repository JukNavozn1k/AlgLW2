import networkx as nx
import matplotlib.pyplot as plt

def has_cycle(graph):
    visited = set()
    rec_stack = set()
    def dfs(node):
        if node in rec_stack:
            return True

        if node in visited:
            return False

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.neighbors(node):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    for node in graph.nodes():
        if dfs(node):
            return True

    return False

G = nx.DiGraph()
G.add_edges_from([(1,2),(2,3),(3,1),(3,4),(2,4)])
title  = ''
if has_cycle(G):
    title = "Циклы есть"
else:
    title = "Циклов нет"


# Print
plt.title(title, fontsize=16, color='blue')
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold', font_size=12)

plt.show()