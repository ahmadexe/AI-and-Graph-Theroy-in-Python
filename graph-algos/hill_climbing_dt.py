graph = {
    1 : [2, 3],
    2 : [1, 4, 5],
    3 : [1, 7, 6],
    4 : [2, 50],
    5 : [2],
    6 : [3],
    7 : [3, 8, 9],
    8 : [7],
    9 : [7],
    50: [4],
}

visited = {}
output = []


def hcl (source):
    global graph, visited, output
    
    for node in graph.keys():
        visited[node] = False
    
    q = []
    visited[source] = True
    q.append(source)

    while len(q) != 0:
        node = q.pop()
        max = node
        output.append(node)
        for neighbour in graph[node]:
            if max < neighbour:
                max = neighbour
                if len(q) != 0:
                    q = []
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
                    

def main():
    source = 1
    hcl(source)
    print("Heelo")
    print(output)
    
if __name__ == "__main__":
    main()