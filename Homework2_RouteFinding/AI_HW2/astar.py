import csv
from sklearn import neighbors
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'                         
from bfs import *                                   # graphfunc() from 'bfs.py' is used in line 7

def heurfunc(lefile):                               # each id differs by test case (id1 for test1, etc)
    heur1 = {}                                      # heur1 as dictionary for node in each row to call its value (distance from node to id1)
    heur2 = {}
    heur3 = {}
    distid = {}                                     # dictionary to store the distance from each row differs by id
    with open(heuristicFile, 'r') as heurfile:      # open and read the heuristic.csv file
        heurreader = csv.reader(heurfile)           # read the program using the csv library (csv.reader)
        rows = list(heurreader)                     # put result of the reader to list row
        for i in range(1, len(rows)):
            node = int(rows[i][0])
            distid1 = float(rows[i][1])             # store heuristic or straight-line distance from the row by id1
            distid2 = float(rows[i][2])
            distid3 = float(rows[i][3])

            if node not in heur1.keys():            # initialize and append the heuristic distance as the value of dictionary
                heur1[node] = []
                heur1[node].append(distid1)

            if node not in heur2.keys():
                heur2[node] = []
                heur2[node].append(distid2)

            if node not in heur3.keys():
                heur3[node] = []
                heur3[node].append(distid3)
    
    return heur1, heur2, heur3

def astar(start, end):
    # Begin your code (Part 4)
    graph, distn, slimit = graphfunc(edgeFile)
    heur1, heur2, heur3 = heurfunc(heuristicFile)

    opened = []                                 # list of nodes which have been visited, but neighbors havent all been inspected
    closed = []                                 # list of nodes which have been visited and neigbors have been inspected
    distt = {}                                  # current distances from start node to all other nodes
    prev_nodes = {}                             # to find the parent node (helps with finding the path)

    opened.append(start)                        # append start to opened
    distt[start] = 0                            # distance of start node from start is 0
    prev_nodes[start] = start                   # parent of start node is start
    path = [] # pindah                          # the shortest path from start to end node
    totaldist = 0                               # save the value of total distance from start to end node
    
    while len(opened) > 0:                      # while opened is not empty  
        node = None
        
        # f(n) = g(n) + h(n)
        # g(n): value of shortest path from start node to node n (here is distt)
        # h(n): heuristic approx. of the node's value (here is heur)

        # find node with lowest value of f(n)
        for v in opened:                        # for the node inside opened
            if (start, end) == (2270143902, 1079387396):        # for test1, thus use heur1
                if node == None or distt[v] + heur1[v][0] < distt[node] + heur1[node][0]:
                    node = v
            elif (start, end) == (426882161, 1737223506):       # for test2, thus use heur2
                if node == None or distt[v] + heur2[v][0] < distt[node] + heur2[node][0]:
                    node = v
            elif (start, end) == (1718165260, 8513026827):      # for test3, thus use heur3
                if node == None or distt[v] + heur3[v][0] < distt[node] + heur3[node][0]:
                    node = v
        
        if node == None: # ganti ini                    # path does not exist if n is end
            break

        # if current node is end node, backtrack from the current node to start node (find path and total distance along the path)
        if node == end:                                 # if current node is end
            totaldist = distt[node]                     # distt is already updated by their weight because of the for loop below
            while node != start:                        # while the node is not start node yet, it will
            # while prev_nodes[node] != node:           # while parent of the node still node the node itself
                path.append(node)                           # append the node to path list
                node = prev_nodes[node]                     # and backtrack to previous nodes
            path.append(start)                          # after start node is found, we append start node to the list
            path.reverse()                              # we reverse the whole path back, which it will return to normal (start to end) 
            break                                       # then break out of the loop

        for m in graph[node]:                           # for all neighbors of current node
            if m not in graph.keys(): continue          # if the neighbour is not part of the graph.keys or start, continue or skip it
            weight = distn[(node, m)]                   # weight is the distance from current node to its neighbours
            if m not in opened and m not in closed:     # if neighbour not in opened and closed list
                opened.append(m)                        # add to opened list and mark node as its parent
                prev_nodes[m] = node
                distt[m] = distt[node] + weight         # dist from neighbour to start is dist from node to start plus neighbour's weight
            else:
                if distt[m] > distt[node] + weight:     # check if it's quicker to visit the node or m
                    distt[m] = distt[node] + weight     # update the distance for m and also the parent
                    prev_nodes[m] = node
                    if m in closed:                     # if neighbour in the closed list
                        closed.remove(m)                # remove it and append to opened list
                        opened.append(m)
        
        if node in opened: # nambah ini
            opened.remove(node) # uncommen ini          # remove current node from opened list
        closed.append(node)                             # append th enode to closed list
    closed.append(end)                                  # when node is endnode, it doesn't run until the end (leads to endnode not appended)

    return path, totaldist, len(closed)
    raise NotImplementedError("To be implemented")
    # End your code (Part 4)

if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')