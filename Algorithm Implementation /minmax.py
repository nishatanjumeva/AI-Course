# --------------------------
# User Input Part
# --------------------------
depth = int(input("Enter depth binary of tree: "))
num_leaf = 2 **depth

# Allocate full size list for 1-based full binary tree indexing
size = 2**(depth + 1)  # total nodes including internal nodes
scores = [None] * size    # index 0 unused

print(f"Enter values for {num_leaf} leaf nodes:")
for i in range(num_leaf):
    val = int(input(f"Leaf node {i+1}: "))
    scores[2**depth + i] = val  # assign leaf node values to correct indices

def minmax(node, depth, isMax, scores):
    """
    node : current node index in scores list
    depth : current depth of tree
    isMax : True if MAX player, False if MIN player
    scores: full list of leaf node scores (1-based indexing)
    """
    # Terminal condition: leaf node
    if depth == 0:
        return scores[node]

    if isMax:
        left = minmax(2*node, depth-1, False, scores)
        right = minmax(2*node+1, depth-1, False, scores)
        return max(left, right)
    else:
        left = minmax(2*node, depth-1, True, scores)
        right = minmax(2*node+1, depth-1, True, scores)
        return min(left, right)


# Run Min-Max
best_score_max = minmax(1, depth, True, scores)
print("Best score for MAX player:", best_score_max)
