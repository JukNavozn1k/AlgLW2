from collections import deque
import networkx as nx
import matplotlib.pyplot as plt



# Стандартный поиск в ширину
def bfs(graph, start):
    visited = {node: False for node in graph}
    distances = {node: float('inf') for node in graph}

    queue = deque()
    queue.append(start)
    visited[start] = True
    distances[start] = 0

    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    return distances


# Находит максимальное расстояние от вершины A до соседей
# Повторяет предыдущий шаг для оставшихся вершин и возвращает максимальное значение.
def graph_diameter(graph):
    max_diameter = 0

    for node in graph:
        distances = bfs(graph, node)
        max_distance = max(distances.values())
        max_diameter = max(max_diameter,max_distance)
    return max_diameter



# Тестовый граф
graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1,2],
    
}
diameter = graph_diameter(graph)


# Визуализация графа
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

plt.figure(figsize=(8, 6))
plt.title(f"Диаметр графа: {diameter}", fontsize=16, color='blue')
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12)

plt.show()
