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



def dfs(source):
    distance = {}
    visited = {}
    parent = {}
    dfs_output = []
    for node in graph.keys():
        distance[node] = -1
        visited[node] = False
        parent[node] = None
    
    stack = []
    stack.append(source)
    visited[source] = True
    distance[source] = 0
    parent[source] = None
    while len(stack) != 0:
        node = stack.pop()
        dfs_output.append(node)
        for child in graph[node]:
            if not visited[child]:
                # print(graph[node], child)
                visited[child] = True
                distance[child] = distance[node] + 1
                parent[child] = node
                stack.append(child)
    
    return dfs_output

def main():
    print(dfs('A'))
    
if __name__ == '__main__':
    main()

    
