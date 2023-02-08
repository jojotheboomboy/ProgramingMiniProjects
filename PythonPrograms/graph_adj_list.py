from logging import PlaceHolder
from queue import Queue
#Graphs

class Graph: 

    def __init__(self):
        self.vertexList = {} 
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):        # self = newVertex, key - 0
            self.id = key               # newVertex.id = 0
            self.connectedTo = {}

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys() #dictionary of key value pairs, other nodes you can travel to and the weight associated with traveling

        def getWeight(self, nbr): 
            return self.connectedTo[nbr]        #v0.connecteTo[1] = 5

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight 

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"


    def addVertex(self, key):           # self = graph / key = 0
        self.numVertices += 1           # 1
        newVertex = Graph.__Vertex(key)     # key = 0
        self.vertexList[key] = newVertex    # graph.verList[0] = newVertex / key = 0
        return newVertex

    def getVertex(self, n):
        if n in self.vertexList: 
            return self.vertexList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertexList

    def addEdge(self, source, destination, weight = 0):        #self = graph, source = 0, dest = 1, weight = 5
        if source not in self.vertexList:
            newVertex = self.addVertex(source)

        if destination not in self.vertexList:
            newVertex = self.addVertex(destination)

        self.vertexList[source].addNeighbor(self.vertexList[destination], weight) # graph.verlist[0].addNeighbor(graph.verlist[1], 5)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    #DFS
    def dfs(self, s, visited = None):
        if visited == None:
            visited = set()         # empty set
        if s not in visited:
            print(s, end=" ")
            visited.add(s)
            for next_node in [x.id for x in self.vertexList[s].connectedTo]:
                self.dfs(next_node, visited)

    def bfs(self, s, visited = None):
        if visited is None:
             visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.vertexList[current_node].connectedTo]:
               # if next_node needs more lines
               PlaceHolder




def main():

    graph = Graph()

    for i in range(6):
        graph.addVertex(i)
        print(graph.numVertices)

    print(graph.vertexList)
    print()

    graph.addEdge(0, 1, 5)      #self = graph
    graph.addEdge(0, 5, 2)

    graph.addEdge(1, 2, 4)

    graph.addEdge(2, 3, 9)

    graph.addEdge(3, 4, 7)
    graph.addEdge(3, 5, 3)
    
    graph.addEdge(4, 0, 1)
    
    graph.addEdge(5, 4, 8)
    graph.addEdge(5, 2, 1)
    

    for vertex in graph:
        for adjacent in vertex.getConnections():
            print(f"({vertex.getId()}, {adjacent.getId()})")

    
    print()

    for k, v in graph.vertexList.items():
        print(k, v)

    print()
    graph.dfs(5)
    
    print()
    graph = Graph()

    for i in range(5):
        graph.addVertex(i)

    graph.addEdge(0, 1, 0)
    graph.addEdge(1, 0, 0)

    graph.addEdge(0, 2, 0)
    graph.addEdge(2, 0, 0)

    graph.addEdge(2, 3, 0)
    graph.addEdge(3, 2, 0)

    graph.addEdge(3, 4, 0)
    graph.addEdge(4, 3, 0)

    graph.addEdge(3, 1, 0)
    graph.addEdge(1, 3, 0)

    for vertex in graph:
        for adjacent in vertex.getConnections():
            print(f"({vertex.getId()}, {adjacent.getId()})")

    print()
    for k, v in graph.vertexList.items():
        print(k, v)

main()
