def is_safe(color, graph, colors, node):
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
    return True

def map_coloring(graph, color_list, colors, nodes):
    if not nodes:
        return True

    node = nodes[0]

    for color in color_list:
        if is_safe(color, graph, colors, node):
            colors[node] = color

            if map_coloring(graph, color_list, colors, nodes[1:]):
                return True

            del colors[node]

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color_list = ['Red', 'Green', 'Blue']
colors = {}

if map_coloring(graph, color_list, colors, list(graph)):
    print("Map Coloring Solution:")
    print(colors)
else:
    print("No solution exists")
