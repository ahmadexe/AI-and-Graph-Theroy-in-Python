import sys
sys.setrecursionlimit(10000)

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E', 'F'],
    'C' : ['A', 'G', 'H'],
    'D' : ['A', 'I', 'J'],
    'E' : ['B', 'K', 'L'],
    'F' : ['B'],
    'G' : ['C'],
    'H' : ['C'],
    'I' : ['D'],
    'J' : ['D', 'M', 'N'],
    'K' : ['E', 'X', 'Y'],
    'L' : ['E'],
    'M' : ['J'],
    'N' : ['J'],
    'X' : ['K'],
    'Y' : ['K'],
}

def ids(source, goal, depthLimit):
    distance = {}
    visited = {}
    parent = {}
    depth = {}
    dfs_output = []
    
    for node in graph.keys():
        distance[node] = -1
        depth[node] = -1
        visited[node] = False
        parent[node] = None
    
    stack = []
    stack.append(source)
    visited[source] = True
    depth[source] = 0
    distance[source] = 0
    parent[source] = None
    currentDepth = 0
    while len(stack) != 0:
        node = stack.pop()
        dfs_output.append(node)
        
        for child in graph[node]:
            currentDepth = depth[node] + 1
            if child == goal:
                return currentDepth
            if currentDepth <= depthLimit:
                if not visited[child]:
                    visited[child] = True
                    depth[child] = depth[node] + 1
                    parent[child] = node
                    stack.append(child)
    return -1


def main():
    for i in range(100):
        depth = ids('A', 'X', i)
        if depth != -1:
            print(depth)
            return None
    print(-1)
            
    
if __name__ == '__main__':
    main()