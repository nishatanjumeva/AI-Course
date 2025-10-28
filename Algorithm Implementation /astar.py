#A* star search
import heapq

# Step 1: Build the graph
graph = {}
cost = {}        # edge costs
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors
    edge_costs = list(map(int, input(f"Edge costs for {node}'s neighbors (space separated): ").split()))
    cost[node] = {neighbors[i]: edge_costs[i] for i in range(len(neighbors))}
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

# Step 2: A* Search function
def a_star_search(start, goal):
    visited = []    # visited nodes list
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, start, [start]))  # (f, g, node, path)

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.append(current)
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            print("Visited nodes in order:", visited)
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                g_new = g + cost[current][neighbor]
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_new, g_new, neighbor, path + [neighbor]))

    print("\nGoal not reachable.")
    print("Visited nodes in order:", visited)

# Step 3: Run the search
start = input("Start node: ")
goal = input("Goal node: ")
a_star_search(start, goal)
