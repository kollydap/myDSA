class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self,vertex,edge):
        '''
        Adds Edge to A given Vertex
        '''
        self.gdict[vertex].append(edge)

dt = {"a":["b","c"],
    "b":["a","d","e"],
    "c":["a","e"],
    "d":["b","e","f"],
    "e":["d","f","c"],
    "f":["d","e"]
}
gp = Graph(dt)
gp1 = Graph()
gp1.addEdge("a","k")
print(gp1.gdict)