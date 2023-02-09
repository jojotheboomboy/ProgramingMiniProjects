from queue import Queue
import sys

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"   

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
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

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):
        list2 = []
        list = []
        helper = set()
        vertices_sets = set()
        edges_dict = dict()
        MST = set()

        # debugging : prints memory location of everything in self.verList
        #print(self.verList)

        # debugging: length of self.verList is 6
        #print(len(self.verList)) 

        #creates a vertices list
        for item in self.verList:
            vertices_sets.add(self.getVertex(item))
        
        for obj in vertices_sets:
            # creates helpers set of all orgin id's
            helper.add(obj.getId()) 
            for compare in obj.getConnections():

                # boolean expresion that will be used to check if an edge's parent vertex's 
                # have already appeard the dictionary in the reverse order
                copy = False 

                # current tuple
                curr = obj.getId(), compare.getId()

                #reverse tuple
                opposite = compare.getId(), obj.getId()

                #reverse tuple list
                list.append(opposite)

                # checks to see if the reverse tuple list contains the current tuple, if so,
                # it will change to copy to true and it's tuple nor it's weight will be added to the dictionary.
                for i in range (len(list)):
                    if curr == list[i]:
                        copy = True
                        break

                # if copy remains false --> no reverse exists, thus it shall be stored in the dictionary.
                if copy == False:

                    #stores respective weight at with curr tuple as key.
                    edges_dict[obj.getId(), compare.getId()] = obj.getWeight(compare)

                    #dubugging
                    print("orgin:{} \t  neighbor:{} \t weight:{} ".format(obj.getId(), compare.getId(), edges_dict[obj.getId(), compare.getId()]))   

        #sorts dictionary in terms of weight
        # Used Code found here <https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value>
        edges_dict = (dict(sorted(edges_dict.items(), key=lambda item: item[1])))

        #debugging: prints the fully filtered dictionary.
        print(edges_dict)

        return MST

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))       # no difference in weight dependent on which direction traveling.
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()
    ### WRITE YOUR CODE HERE ###
    #for vertex in graph:
    #    for adjacent in vertex.getConnections():
    #        print(f"({vertex.getId()}, {adjacent.getId()})")
    print("Graph adjacency list:")
    for l, s in graph.verList.items():
        print(l, s)
    
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    
    
'''
        #for i in range(len(self.verList)):
            #vertices_sets.add(i)
            #print(self.getVertex())
        #print(self.verList.items())

        #for curr in self.verList:
            #vertices_sets.add(curr)
            #print(self.verList.items())
            #vertices_sets.add(self.verList.items())
            #print(vertices_sets)
            
        #print(self.getConnections())
        
        #print(vertices_sets)
        #print(len(self.verList))

        #print(item)
            #print(type(item))
            
            #print(self.verList[item])
            #print(type(self.verList[item]))


        #for e in self.verList:
            
        
            #print(type(self.verList[item]))
            #vertices_sets[item] = k
            #print(item)
            #print(type(item))

        ### WRITE YOUR CODE HERE ###
        #for l, s in self.verList.items():
            #vertices_sets.add(l)
            #print(l)
            #edges_dict[l] = s  
            #print("done")

        #print(vertices_sets)
        #for x in vertices_sets:
            #print(type(x))
            #print(x)
        '''