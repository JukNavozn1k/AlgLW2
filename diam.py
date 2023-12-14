from collections import deque

# Function to perform Breadth First Search (BFS)
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

# Function to find the diameter of the graph
def graph_diameter(graph):
    max_diameter = 0

    for node in graph:
        distances = bfs(graph, node)
        max_distance = max(distances.values())
        if max_distance > max_diameter:
            max_diameter = max_distance

    return max_diameter

# Define your graph (adjacency list representation)
# Replace this with your own graph structure
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4],
    
}

# Calculate the diameter of the graph
diameter = graph_diameter(graph)

print(f"The diameter of the graph is: {diameter}")
