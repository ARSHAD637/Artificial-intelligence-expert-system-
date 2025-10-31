# Map Coloring Problem (Australia Map)

# Adjacency representation (graph)
graph = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales', 'Tasmania'],
    'Tasmania': ['Victoria']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store assigned colors
color_assignment = {}

def is_safe(region, color):
    """Check if assigning this color to region is valid."""
    for neighbor in graph[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def color_map(region_index, regions):
    """Backtracking function to color the map."""
    if region_index == len(regions):
        return True
    
    region = regions[region_index]
    for color in colors:
        if is_safe(region, color):
            color_assignment[region] = color
            if color_map(region_index + 1, regions):
                return True
            # Backtrack
            del color_assignment[region]
    return False

regions = list(graph.keys())

if color_map(0, regions):
    print("✅ Map Coloring Solution:")
    for region, color in color_assignment.items():
        print(f"{region}: {color}")
else:
    print("❌ No valid coloring found.")




ouput:
✅ Map Coloring Solution:
Western Australia: Red
Northern Territory: Green
South Australia: Blue
Queensland: Red
New South Wales: Green
Victoria: Red
Tasmania: Green

