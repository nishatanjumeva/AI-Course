def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

# adjacency list: index 0 unused, nodes are 1..n
graph = [[] for _ in range(n + 1)]

print("Enter each edge as: u v (space separated)")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  # edge u -> v

start = int(input("Start node: "))

# Perform DFS
visited = dfs(graph, start, [])
print("Visited nodes in DFS order:", visited)
