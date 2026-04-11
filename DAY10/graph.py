class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            # self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,"->",self.adjacency_list[vertex])
    
    
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("B","A")
graph.add_edge("B","E")
graph.add_edge("C","A")
graph.add_edge("C","E")
graph.add_edge("D","E")
graph.add_edge("D","B")
graph.add_edge("D","F")
graph.add_edge("E","F")
graph.add_edge("E","C")
graph.add_edge("E","D")
graph.add_edge("E","B")
graph.add_edge("F","E")
graph.add_edge("F","D")
graph.print_graph()


