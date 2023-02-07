from queue import Queue

graph = {
    'A' : ['B', 'D'],
    'B' : ['A', 'C'],
    'C' : ['B'],
    'D' : ['A', 'E', 'F'],
    'E' : ['D', 'F', 'G'],
    'F' : ['D', 'E', 'H'],
    'G' : ['E', 'H'],
    'H' : ['G', 'F'],
}

visited = {}
parent = {}
distance = {} 
bfs_traversal_output = []

def bfs(source):
    global graph, visited, parent, distance, bfs_traversal_output
    
    for node in graph.keys():
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
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                distance[neighbour] = distance[node] + 1
                parent[neighbour] = node
                q.put(neighbour)
                

def findPath(destination):
    global parent, bfs_traversal_output
    if destination not in bfs_traversal_output:
        return []
    path = []
    at = destination
    while at is not None:
        path.append(at)
        at = parent[at]
    path.reverse()
    return path

def main():
    bfs("A")
    print(bfs_traversal_output)    


if __name__ == "__main__":
    main()

    