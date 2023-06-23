class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            self.edges = set(edge for edge in self.edges if vertex not in edge)

    def add_edge(self, edge):
        if all(vertex in self.vertices for vertex in edge):
            self.edges.add(edge)

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

    #Алгоритм обхода в глубину для проверки связности
    def is_connected(self):
        visited = set()
        stack = [next(iter(self.vertices))]

        while stack:
            vertex = stack.pop()
            visited.add(vertex)

            for edge in self.edges:
                if vertex in edge:
                    neighbor = next(v for v in edge if v != vertex)
                    if neighbor not in visited:
                        stack.append(neighbor)

        return len(visited) == len(self.vertices)