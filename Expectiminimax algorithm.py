# Simple Expectiminimax Tree Implementation

class Node:
    def __init__(self, node_type, children=None, probs=None, value=None):
        self.node_type = node_type   # 'max', 'min', 'chance', 'leaf'
        self.children = children or []
        self.probs = probs or []     # Used by chance nodes
        self.value = value

def expectiminimax(node):
    if node.node_type == 'leaf':
        return node.value
    elif node.node_type == 'max':
        values = [expectiminimax(child) for child in node.children]
        return max(values)
    elif node.node_type == 'min':
        values = [expectiminimax(child) for child in node.children]
        return min(values)
    elif node.node_type == 'chance':
        values = [expectiminimax(child) for child in node.children]
        weighted = sum(p * v for p, v in zip(node.probs, values))
        return weighted

# Build tree from diagram:
# Root (MAX)
#   Chance Node: [Leaf(1), Leaf(2)] with probs [0.3, 0.7]
#   Min Node: [Leaf(2), Leaf(4)]

leaf1 = Node('leaf', value=1)
leaf2 = Node('leaf', value=2)
leaf4 = Node('leaf', value=4)

chance_node = Node('chance', children=[leaf1, leaf2], probs=[0.3, 0.7])
min_node = Node('min', children=[leaf2, leaf4])

root = Node('max', children=[chance_node, min_node])

# Compute values
root_value = expectiminimax(root)
chance_value = expectiminimax(chance_node)
min_value = expectiminimax(min_node)

print("Expected utility at Chance Node:", chance_value)
print("Utility at Min Node:", min_value)
print("Expected utility at root (Max):", root_value)

# Show effect of randomness: change probabilities
chance_node2 = Node('chance', children=[leaf1, leaf2], probs=[0.9, 0.1])
root2 = Node('max', children=[chance_node2, min_node])
root2_value = expectiminimax(root2)
print("Changed probabilities at Chance Node: [0.9, 0.1]")
print("Expected utility at root (Max):", root2_value)

# Optimal decision
if chance_value > min_value:
    print("AI chooses Chance subtree (expected utility = {:.2f})".format(chance_value))
else:
    print("AI chooses Min subtree (utility = {:.2f})".format(min_value))


output:
Expected utility at Chance Node: 1.7
Utility at Min Node: 2
Expected utility at root (Max): 2
Changed probabilities at Chance Node: [0.9, 0.1]
Expected utility at root (Max): 2
AI chooses Min subtree (utility = 2.00)

