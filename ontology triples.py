# Step 1: Parse ontology triples
triples = [
    ("LivingThing", "subclass_of", "Entity"),
    ("Animal", "subclass_of", "LivingThing"),
    ("Dog", "subclass_of", "Animal"),
    ("Cat", "subclass_of", "Animal")
]

# Step 2: Build knowledge graph (dictionary where parent -> set of children)
from collections import defaultdict, deque

graph = defaultdict(set)
for child, rel, parent in triples:
    if rel == "subclass_of":
        graph[parent].add(child)

# Step 3: Query functions
def find_subclasses(graph, parent):
    subclasses = set()
    queue = deque([parent])
    while queue:
        cls = queue.popleft()
        for sub in graph.get(cls, []):
            if sub not in subclasses:
                subclasses.add(sub)
                queue.append(sub)
    return subclasses

def is_subclass(graph, child, ancestor):
    # BFS/DFS upward: find if ancestor is reachable from child by inverse relations
    parent_map = defaultdict(set)
    for par, children in graph.items():
        for c in children:
            parent_map[c].add(par)
    visited = set()
    stack = [child]
    while stack:
        n = stack.pop()
        if n == ancestor:
            return True
        for p in parent_map.get(n,[]):
            if p not in visited:
                visited.add(p)
                stack.append(p)
    return False

# Step 4: Print results

print("Ontology Graph (parent -> subclasses):")
for k,v in graph.items():
    print(f"  {k}: {sorted(v)}")

query_class = "Animal"
all_subs = find_subclasses(graph, query_class)
print(f"\nAll subclasses of '{query_class}': {all_subs}")

check_sub = "Dog"
check_anc = "LivingThing"
print(f"Is '{check_sub}' a subclass of '{check_anc}'? {is_subclass(graph, check_sub, check_anc)}")

check_sub2 = "Cat"
check_anc2 = "Entity"
print(f"Is '{check_sub2}' a subclass of '{check_anc2}'? {is_subclass(graph, check_sub2, check_anc2)}")


output:
Ontology Graph (parent -> subclasses):
  Entity: ['LivingThing']
  LivingThing: ['Animal']
  Animal: ['Cat', 'Dog']

All subclasses of 'Animal': {'Dog', 'Cat'}
Is 'Dog' a subclass of 'LivingThing'? True
Is 'Cat' a subclass of 'Entity'? True
