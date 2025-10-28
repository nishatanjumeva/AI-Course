def dls(graph, node, path, visited_order, limit, goal, depth=0):
    if depth > limit:
        return False

    path.append(node)               
    visited_order.append(node)    

    if node == goal:
        return True

    for neighbor in graph[node]:
        if neighbor not in path: 
            found = dls(graph, neighbor, path, visited_order, limit, goal, depth + 1)
            if found:
                return True

    path.pop()  
    return False


def iddls(graph, start, goal, max_depth):
    visited_order = []  
    for limit in range(max_depth + 1):
        path = []
        visited_order.clear()  
        found = dls(graph, start, path, visited_order, limit, goal)

        if found:
            break

    return visited_order


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
max_depth = int(input("Maximum depth limit: "))

visited_path = iddls(graph, start, goal, max_depth)

print("\nVisited path:", visited_path)

if goal in visited_path:
    print(f"Goal node {goal} was found!")
else:
    print(f"Goal node {goal} not found within maximum depth {max_depth}.")
