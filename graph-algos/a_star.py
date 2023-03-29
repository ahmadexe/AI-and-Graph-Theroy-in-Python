import math

graph = {
    'A': [['F', 1]],
    'F': [['A', 1], ['H', 1]],
    'H': [['F', 1], ['M', 1], ['I', 1]],
    'M': [['R', 1], ['N', 1], ['H', 1]],
    'R': [['S', 1], ['M', 1]],
    'S': [['R', 1], ['N', 1]],
    'N': [['S', 1], ['M', 1], ['I', 1]],
    'I': [['N', 1], ['H', 1]],
    'W': [['T', 1]],
    'T': [['W', 1], ['S', 1], ['U', 1]],
    'J': [['I', 1], ['G', 1]],
    'G': [['J', 1], ['B', 1]],
    'B': [['G', 1], ['C', 1]],
    'U': [['T', 1], ['O', 1]],
    'O': [['U', 1], ['P', 1]],
    'C': [['B', 1], ['D', 1]],
    'X': [['Y', 1]],
    'P': [['Q', 1], ['K', 1]],
    'K': [['P', 1], ['L', 1]],
    'D': [['C', 1], ['E', 1]],
    'Y': [['X', 1], ['V', 1]],
    'V': [['Y', 1], ['Q', 1]],
    'Q': [['V', 1], ['P', 1], ['L', 1]],
    'L': [['Q', 1], ['K', 1]],
    'E': [['D', 1]],
}

location = {
    'A': [0,0],
    'F': [1, 0],
    'H': [2, 0],
    'M': [3, 0],
    'R': [4, 0],
    'S': [4, 1],
    'N': [3, 1],
    'I': [2, 1],
    'W': [5, 2],
    'T': [4, 2],
    'J': [2, 2],
    'G': [1, 2],
    'B': [0, 1],
    'U': [4, 3],
    'O': [3, 3],
    'C': [0, 3],
    'X': [5, 4],
    'P': [3, 4],
    'K': [2, 4],
    'D': [0, 4],
    'Y': [5, 5],
    'V': [4, 5],
    'Q': [3, 5],
    'L': [2, 5],
    'E': [0, 5],
}


heuristic = dict()

cost = {'A': 0}    

def buildGraph():
    global graph
    numNodes = int(input('Enter number of nodes: '))
    for i in range(numNodes):
        node = input('Enter node name: ')
        numChildren = int(input('Enter number of children: '))
        children = []
        for j in range(numChildren):
            child = input('Enter child name: ')
            cost = int(input('Enter cost: '))
            children.append([child, cost])
        graph.update({node: children})
         


def populateHeuristics():
    global heuristic
    for node in location:
        heuristic.update({node: math.sqrt((location[node][0] - location['Y'][0]) ** 2 + (location[node][1] - location['Y'][1]) ** 2)})
    
    
def AStarSearch():
    global graph, heuristic
    searchedPath = []             
    pathToSearch = [['A', heuristic['A']]]     

    while True:
        fn = [i[1] for i in pathToSearch]
        chosen_index = fn.index(min(fn))
        node = pathToSearch[chosen_index][0]  
        searchedPath.append(pathToSearch[chosen_index])
        del pathToSearch[chosen_index]
        if searchedPath[-1][0] == 'Y':        
            break
        for item in graph[node]:
            if item[0] in [searchedPath_item[0] for searchedPath_item in searchedPath]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            
            fn_node = cost[node] + heuristic[item[0]] + item[1]     
            temp = [item[0], fn_node]
            pathToSearch.append(temp)                                     


    searchedPath.append(['Y', 0])
    traceNode = 'Y'                        
    optimalSequence = ['Y']                
    for i in range(len(searchedPath)-2, -1, -1):
        check_node = searchedPath[i][0]           
        if traceNode in [children[0] for children in graph[check_node]]:
            childrenCosts = [temp[1] for temp in graph[check_node]]
            children_nodes = [temp[0] for temp in graph[check_node]]

            if cost[check_node] + childrenCosts[children_nodes.index(traceNode)] == cost[traceNode]:
                optimalSequence.append(check_node)
                traceNode = check_node
    optimalSequence.reverse()            

    return searchedPath, optimalSequence


if __name__ == '__main__':
    populateHeuristics()
    _, path = AStarSearch()
    print('Path: ' + str(path))