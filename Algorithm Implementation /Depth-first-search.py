from collections import deque         

def bfs(graph, start, visited):
                          
    queue   = deque([start])          

    while queue:                       
        node = queue.popleft()        
        if node not in visited:        
            visited.append(node)        
            
            for i in graph[node]:
                if i not in visited and i not in queue:
                    queue.append(i)

    return visited

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

# adjacency list: index 0 unused, nodes are 1..n
graph = [[] for _ in range(n + 1)]

print("Enter each edge as: u v (space separated)")
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)         

start = int(input("Start node: "))

# Perform BFS
visited = bfs(graph, start,[])
print("Visited nodes in BFS order:", visited)
