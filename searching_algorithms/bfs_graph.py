from dfs_graph import numbered_graph
from queue import SimpleQueue

def bfs(graph, initial_vertex):
    visited_vertices = []

    bfs_queue = SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)

    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()

        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    
    return visited_vertices

print(bfs(numbered_graph(), '0')) # ['0', '1', '2', '3', '4']
