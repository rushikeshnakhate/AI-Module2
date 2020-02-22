def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []
queue = []
for n in graph['A']:
    if n not in visited:
        visited.append(n)
        queue.append(n)

# bfs(visited, graph, 'A')
