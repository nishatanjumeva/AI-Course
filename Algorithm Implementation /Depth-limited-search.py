def dls(graph, node, visited, limit, goal, depth=0):
    
    if depth > limit:   
        return False

    visited.append(node)

    if node == goal:         
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            found = dls(graph, neighbor, visited, limit, goal, depth + 1)
            if found:         
                return True
    
    return False            


# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

graph = [[] for _ in range(n + 1)]

print("Enter each edge as: u v (space separated)")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  

start = int(input("Start node: "))
goal = int(input("Goal node: "))
limit = int(input("Depth limit: "))

visited = []
found = dls(graph, start, visited, limit, goal)

print("Visited nodes (within depth limit):", visited)
if found:
    print(f"Goal node {goal} was found!")
else:
    print(f"Goal node {goal} not found within depth {limit}.")
