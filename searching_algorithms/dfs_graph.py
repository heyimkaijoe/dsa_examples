class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)

def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)

        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)

g = Graph()

g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')

g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('1', '0')
g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '0')
g.add_edge('2', '1')
g.add_edge('2', '4')
g.add_edge('3', '1')
g.add_edge('3', '4')
g.add_edge('4', '2')
g.add_edge('4', '3')

dfs(set(), g.vertices, '0') # print order: 0->1->2->4->3
