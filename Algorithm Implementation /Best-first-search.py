from heapq import heappush, heappop

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heappush(pq, (heuristic[start], start))
    parent = {start: None}

    while pq:
        _, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                heappush(pq, (heuristic[neighbor], neighbor))
    return None

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

graph = {}
print("Enter each edge as: u v (space separated, node names can be int or str)")
for _ in range(m):
    u, v = input().split()
    # Use string labels for nodes
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

heuristic = {}
print("Enter heuristic values (node h):")
for node in graph:
    h = int(input(f"h({node}): "))
    heuristic[node] = h

start = input("Start node: ")
goal = input("Goal node: ")

path = best_first_search(graph, start, goal, heuristic)
print("Best-First Path:", path)
