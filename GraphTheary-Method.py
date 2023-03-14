# 1st task - Create a class that creates a vertex and edge
class Graph:
    def __init__(self):
        self.graph_dict = {}
        
    def add_vertex(self, vertex: str):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append((vertex2, weight))
        else:
            self.graph_dict[vertex1] = [(vertex2, weight)]
            
    def get_edges(self, vertex):
        return self.graph_dict[vertex]
        
# Create some vertex

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('V')
graph.add_vertex('P')

graph.add_edge('A', 'V', 4)
graph.add_edge('A', 'P', 7)
graph.add_edge('V', 'P', 7)

print(graph.get_edges('A'))

# 2nd Task - Create a function that hops between 2 vertecies. 
