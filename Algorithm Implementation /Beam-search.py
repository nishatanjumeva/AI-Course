from heapq import heappush, heappop

def beam_search(graph, start, goal, heuristic, beam_width):
    frontier = [(heuristic[start], start, [start])]
    visited = set()

    while frontier:
        new_frontier = []
        for _, node, path in frontier:
            if node == goal:
                return path
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heappush(new_frontier, (heuristic[neighbor], neighbor, path + [neighbor]))

        frontier = []
        for _ in range(min(beam_width, len(new_frontier))):
            frontier.append(heappop(new_frontier))

    return None

# ---- Input ----
n = int(input("Number of nodes (n): "))
m = int(input("Number of edges (m): "))

graph = {}
print("Enter each edge as: u v")
for _ in range(m):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

heuristic = {}
print("Enter heuristic values (node h):")
for node in graph:
    heuristic[node] = int(input(f"h({node}): "))

start = input("Start node: ")
goal = input("Goal node: ")
beam_width = int(input("Beam width: "))

path = beam_search(graph, start, goal, heuristic, beam_width)
print("Beam Search Path:", path)
