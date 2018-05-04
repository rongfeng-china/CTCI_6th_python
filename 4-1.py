# Python program to detect cycle 
# in a graph

from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.visited = [0]*self.V

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def search(self,start,end):
        if start == end:
            return True
        else:
            result = False
            for neighbor in self.graph[start]:
                if self.visited[neighbor] == 0:
                    self.visited[neighbor] = 1
                    result = result or self.search(neighbor,end)
            return result
    
    def renew_visited(self):
        self.visited = [0]*self.V
                    
g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
result = g.search(3,0)
print (result)

g.renew_visited()
result = g.search(1,0)
print (result)



















