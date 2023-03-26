graph = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}

heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}

cost = {'S': 0}             


def AStarSearch():
    global graph, heuristic
    searchedPath = []             
    pathToSearch = [['S', 8]]     

    while True:
        fn = [i[1] for i in pathToSearch]
        chosen_index = fn.index(min(fn))
        node = pathToSearch[chosen_index][0]  
        searchedPath.append(pathToSearch[chosen_index])
        del pathToSearch[chosen_index]
        if searchedPath[-1][0] == 'G':        
            break
        for item in graph[node]:
            if item[0] in [searchedPath_item[0] for searchedPath_item in searchedPath]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            
            fn_node = cost[node] + heuristic[item[0]] + item[1]     
            temp = [item[0], fn_node]
            pathToSearch.append(temp)                                     

    traceNode = 'G'                        
    optimalSequence = ['G']                
    for i in range(len(searchedPath)-2, -1, -1):
        check_node = searchedPath[i][0]           
        if traceNode in [children[0] for children in graph[check_node]]:
            childrenCosts = [temp[1] for temp in graph[check_node]]
            children_nodes = [temp[0] for temp in graph[check_node]]

            if cost[check_node] + childrenCosts[children_nodes.index(traceNode)] == cost[traceNode]:
                optimalSequence.append(check_node)
                traceNode = check_node
    optimalSequence.reverse()              # reverse the optimal sequence

    return searchedPath, optimalSequence


if __name__ == '__main__':
    _, path = AStarSearch()
    print('Path: ' + str(path))