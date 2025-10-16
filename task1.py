from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Breadth First Search
def bfs(graph, start):
    visited = set()          # Track visited nodes
    queue = deque([start])   # Queue for BFS
    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()


# Depth First Search (recursive)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:", end=" ")

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Main
if __name__ == "__main__":
    print("Graph:", graph)
    bfs(graph, 'A')   # Starting node A
    dfs(graph, 'A')
  OUTPUT:
Graph: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
BFS Traversal: A B C D E F 
DFS Traversal: A B D E F C 
>>> 
