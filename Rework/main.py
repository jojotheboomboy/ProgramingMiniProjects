import csv
import queue
import sys

class Graph:
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0 
    
    class __Vertex:
        def __init__(self, key) -> None:
            self.id = key
            self.connectedTo = {}

        def getId(self):
            return self.id
        
        def getConnections(self):
            return self.connectedTo.keys()
        
        def getWeight(self, nbr):
            return self.connectedTo[nbr]
        
        def setWeight(self, nbr, x):
            self.connectedTo[nbr] = x
        
        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight
            
        def __str__(self) -> str:
            return f"connected to: {[x.id for x in self.connectedTo]}"
    
    def addVertex(self, key): # self = graph / key = 0
        self.numVertices += 1 # 1
        newVertex = Graph.__Vertex(key) # key = 0
        self.vertList[key] = newVertex # graph.vertList[key] = newVertex / key = 0
        return newVertex
    
    def getVertex(self, n) -> __Vertex:
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList
    
    
    def addEdge(self, source, destination, weight = 999):
        if source not in self.vertList:
            newVertex = self.addVertex(source)
            
        if destination not in self.vertList:
            newVertex = self.addVertex(destination)
            
        self.vertList[source].addNeighbor(self.vertList[destination], weight)
        # graph.vertList[0].addNeighbor(graph.vertList[1], 5)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

    # DFS algo
    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()
        
        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for nest_node in [x.id for x in self.vertList[s].connectedTo]:
                self.dfs(nest_node, visited)
    
    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()
        
        q = queue()
        
        q.put(s)
        visited.add(s)
        while not q.empty():
            current_node = q.get()
            print(current_node, end=" ")
            
            for next_node in [x.id for x in self.vertList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)
    
    # distatnce vector routing function
    def dvr(self):
        
        # s is defined to be a source node (EG: u). s_connections is define to be the set of all nodes (EG: {u,v,w,x,y,z}). 
        # d is defined to be a destination node (EG: w)
        def bellmanFord(s, s_connections, d):
            
            # Set the minimum equal to the weight of the source to the destination
            minimum = s.getWeight(d)
            
            # neighbors will iterate over the set of all nodes (EG: neighbor is a node in {u,v,w,x,y,z})
            for neighbor in s_connections:
                
                # check to make certain that the neighboring node is refrencing the neither a the source node or the a disjointed node.
                if (neighbor.getId() != s.getId() and s.getWeight(neighbor) != 9999):
                    
                    # Checks wether the minimum needs to be updated 
                    if s.getWeight(neighbor) + neighbor.getWeight(d) < minimum:
                        minimum = s.getWeight(neighbor) + neighbor.getWeight(d)
            
            # returns the minimum weight from a source node to a destination node
            return minimum
        
        # establishes a 'vertices_set' to be the set {u,v,w,x,y,z}
        vertices_sets = set()
        for item in self.vertList:
            vertices_sets.add(self.getVertex(item))
        
        # source is a single node in the set {u,v,w,x,y,z}
        for source in vertices_sets:
            
            #made to keep tracl of the weights from one node to another.
            list = []
            
            # destination is a single node in the set {u,v,w,x,y,z}
            for dest in vertices_sets:
                
                # checks to insure source and destination are not the same node.
                if source.getWeight(dest) > 0:
                    
                    # calls bellmanFord equation
                    minimum = bellmanFord(source, vertices_sets, dest)
                    
                    # sets the weight equal to the minimum which is found via the Bellman-Ford equation.
                    source.setWeight(dest, minimum)
                    
                # appends value to the weight list
                list.append((source.getWeight(dest)))
                
            #prints list
            print(source.getId(), list)
        
def main():
    
    # create an empty graph
    graph = Graph()
    
    file = sys.argv[1]
  
    with open(file, mode ='r')as file:
   
        # reading the CSV file
        csvFile = csv.reader(file)
        
        data = []
        for line in csvFile:
            print(line)
            data.append(line)
        # print(data)
        i, j = 1, 1
        MAX = len(line)
        # print(MAX)
        
        while i < MAX:
            while j < MAX:
                # print(data[i][j], end="\t")
                #if data[i][j] in ["0", "9999"]:
                    # print("remove")
                    #j+=1
                    #continue
                graph.addEdge(data[i][0], data[0][j], int(data[i][j]))
                j+=1
            j = 1
            i+=1
            # print("")
    for k, v in graph.vertList.items():
        print(k, v)
        
    graph.dvr()

main() 
    
    
