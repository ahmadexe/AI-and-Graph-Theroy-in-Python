from queue import Queue

class Graph:
    def __init__(self, graph, directed):
        self.graph = graph
        self.directed = directed
    
    def printGraph(self):
        print(self.graph)
     
    def BFS(self, source):
        visited = {}
        parent = {}
        distance = {} 
        bfs_traversal_output = []
        
        for node in self.graph.keys():
            visited[node] = False
            parent[node] = None
            distance[node] = -1
        
        q = Queue()
        visited[source] = True
        distance[source] = 0
        parent[source] = None
        q.put(source)
        
        while not q.empty():
            node = q.get()
            bfs_traversal_output.append(node)
            for child in self.graph[node]:
                if not visited[child]:
                    visited[child] = True
                    distance[child] = distance[node] + 1
                    parent[child] = node
                    q.put(child)
            
        return {
            'output': bfs_traversal_output,
            'parents_list': parent
        }
    
    def getPath(self, source, destination):
        bfs = self.BFS(source)
        parents = bfs['parents_list']
        location = destination
        path = []
        while location is not None:
            path.append(location)
            location = parents[location]
        path.reverse()
        return path
        

     
def main():
    g = {
        'A': ['B', 'E', 'C'],
        'B': ['A', 'E', 'D'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C'],
    }
    graph = Graph(g,False)
    path = graph.getPath("A", "F")
    print(path)
    
if __name__ == "__main__":
    main()   
