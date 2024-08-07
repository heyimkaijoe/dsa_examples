class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target, weight):
        self.vertices[source].append([target, weight])

g = Graph()

g.add_vertex('Taipei')
g.add_vertex('Yilan')
g.add_vertex('Changhua')

g.add_edge('Taipei', 'Yilan', 37)
g.add_edge('Yilan', 'Changhua', 144)
g.add_edge('Changhua', 'Taipei', 148)

print(g.vertices['Taipei'])   # [['Yilan', 37]]
print(g.vertices['Yilan'])    # [['Changhua', 144]]
print(g.vertices['Changhua']) # [['Taipei', 148]]
