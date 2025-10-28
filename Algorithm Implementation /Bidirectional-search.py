from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    queue_forward = deque([start])
    visited_forward = {start: None}
    
    queue_backward = deque([goal])
    visited_backward = {goal: None}

    intersecting_node = None

    while queue_forward and queue_backward:
        # Forward search
        current_forward = queue_forward.popleft()
        
        for neighbor in graph[current_forward]:
            if neighbor not in visited_forward:
                visited_forward[neighbor] = current_forward
                queue_forward.append(neighbor)
                
                if neighbor in visited_backward:
                    intersecting_node = neighbor
                    break
                    
        if intersecting_node:
            break

        # Backward search
        current_backward = queue_backward.popleft()
        
        for neighbor in graph[current_backward]:
            if neighbor not in visited_backward:
                visited_backward[neighbor] = current_backward
                queue_backward.append(neighbor)
                
                if neighbor in visited_forward:
                    intersecting_node = neighbor
                    break
                    
        if intersecting_node:
            break

    if intersecting_node:
        path = []
        node = intersecting_node
        while node is not None:
            path.append(node)
            node = visited_forward[node]
        path.reverse()
        
        # From intersecting node to goal
        node = visited_backward[intersecting_node]
        while node is not None:
            path.append(node)
            node = visited_backward[node]
        
        return path
    
    return None

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

graph = [[] for _ in range(n + 1)]

print("Enter each edge as: u v (space separated)")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Start node: "))
goal = int(input("Goal node: "))

path = bidirectional_search(graph, start, goal)


print("Path found:", path)
