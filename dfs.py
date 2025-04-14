import random  # Import the random module


def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = []
    visited.append(start_node)
    print(start_node, end=" ")

    # Shuffle the neighbors to add randomness
    neighbors = list(graph[start_node])
    random.shuffle(neighbors)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D']
}
print("DFS Traversal:")
dfs(graph, 'A')
