def alphabeta(node, depth, alpha, beta, maximizing_player, values, children):
    if depth == 0 or node not in children:
        return values[node]

    if maximizing_player:
        value = float("-inf")
        for child in children[node]:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False, values, children))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for child in children[node]:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True, values, children))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

# ---- Input ----
n = int(input("Number of nodes: "))
children = {}
values = {}

print("Enter children (parent child1 child2 ...), or -1 if leaf:")
for _ in range(n):
    data = input().split()
    parent = data[0]
    if data[1] == "-1":
        values[parent] = int(input(f"Value of leaf {parent}: "))
    else:
        children[parent] = data[1:]

root = input("Root node: ")
depth = int(input("Depth of tree: "))

score = alphabeta(root, depth, float("-inf"), float("inf"), True, values, children)
print("Alpha-Beta Value:", score)
