import math

class Node: 
    def __init__(self, state, parent, action, totalCost):
        self.state = state
        self.parent = parent
        self.action = action
        self.totalCost = totalCost

def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node

def actionSequence(graph, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent= graph[currentParent].parent
    solution.reverse()
    return solution

def UCS():
    initialState = 'Arad'
    goalState = 'Bucharest'

    graph = {
    'Neamt': Node('Neamt', None, [('Iasi', 87)], 0),
    'Iasi': Node('Iasi', None, [('Neamt', 87), ('Vaslui', 92)], 0),
    'Vaslui': Node('Vaslui', None, [('Urziceni', 142), ('Iasi', 92)], 0),
    'Urziceni': Node('Urziceni', None, [('Vaslui', 142), ('Hirsova', 98), ('Bucharest', 85)], 0),
    'Hirsova': Node('Hirsova', None, [('Urziceni', 98), ('Eforie', 86)], 0),
    'Eforie': Node('Eforie', None, [('Hirsova', 86)], 0),
    'Bucharest': Node('Bucharest', None, [('Urziceni', 85), ('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211)], 0),
    'Giurgiu': Node('Giurgiu', None, [('Bucharest', 90)], 0),
    'Pitesti': Node('Pitesti', None, [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)], 0),
    'Craiova': Node('Craiova', None, [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Drobeta', 120)], 0),
    'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)], 0),
    'Fagaras': Node('Fagaras', None, [('Sibiu', 99), ('Bucharest',211)], 0),
    'Sibiu' : Node('Sibiu', None, [('Fagarus', 99),('Rimnicu Vilcea', 80)], 0),
    'Oradea' : Node('Oradea', None, [('Sibiu',  151),('Zerind', 71)], 0),
    'Zerind' : Node('Zerind', None, [('Arad', 75),('Oradea', 71)], 0),
    'Arad' : Node('Arad', None, [('Zerind', 75),('Sibiu', 140),('Timisoara', 118)], 0),
    'Timisoara' : Node('Timisoara', None, [('Arad', 118),('Lugoj', 111)], 0),
    'Lugoj' : Node('Lugoj', None, [('Timisoara', 111),('Mehadia', 70)], 0),
    'Mehadia' : Node('Mehadia', None, [('Lugoj', 70),('Drobeta', 75)], 0),
    'Drobeta' : Node('Drobeta', None, [('Mehadia', 75),('Craiova', 120)], 0),   
}

    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = []

    while len(frontier)!=0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, goalState)
        
    currentCost = 0
    explored.append(currentNode)
    for child in graph[currentNode].action:
        currentCost += child[1]
        if child[0] not in frontier and child[0] not in explored:
            graph[child[0]].parent = currentNode
            graph[child[0]].totalCost = currentCost
            frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
        elif child[0] in frontier:
            if frontier[child[0]][1] < currentCost:
                graph[child[0]].parent = frontier[child[0]][0]
                graph[child[0]].totalCost = frontier[child[0]][1]
        else:
            frontier[child[0]] = (currentNode, currentCost)
            graph[child[0]].parent = frontier[child[0]][0]
            graph[child[0]].totalCost = frontier[child[0]][1]
          
    return currentCost      
    
solution = UCS()

print (solution)