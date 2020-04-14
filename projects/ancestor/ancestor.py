class Graph:
    def __init__(self):
        self.vertices = {}

    # Adds a vertex to the graph
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    # Adds an edge to the graph --> Checks if v1 and v2 are valid and then adds
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    # Grabs ancestors (edges) of a vertex
    def get_ancestors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise Exception("Vertex ID was not found")


def earliest_ancestor(ancestors, starting_node):
    pass

