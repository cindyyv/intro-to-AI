import csv
edgeFile = 'edges.csv'
from bfs import *                                       # graphfunc() from 'bfs.py' is used in line 7

def ucs(start, end):
    # Begin your code (Part 3)
    graph, distn, slimit = graphfunc(edgeFile)
    queue = []                                          
    visited = []
    distt = {}                                          # dictionary that stores distance from start node to current node
    prev_nodes = {}                                     # to find the parent node (helps with finding the path)

    queue.append(start)                                 # append start to queue
    distt[start] = 0                                    # distance of start node from start is 0
    prev_nodes[start] = start                           # parent of start node is start
    path = []                                           # the shortest path from start to end node
    totaldist = 0                                       # save the value of total distance from start to end node

    while queue:                                        # while queue is not empty
        node = None                                     # initialize node
        for v in queue:                                 # for the node inside queue
            if node == None or distt[v] < distt[node]:  # if node still None or distt from v is smaller than that of current node
                node = v                                # let node be v
        
        if node == None: # ganti ini                    # path does not exist if node is end
            break

        # if current node is end node, backtrack from the current node to start node (find path and total distance along the path)
        if node == end:                                 # if current node is end
            totaldist = distt[node]                     # distt is already updated by their weight because of the for loop below
            while node != start:                        # while the node is not start node yet, it will
                path.append(node)                           # append the node to path list
                node = prev_nodes[node]                     # and backtrack to previous nodes
            path.append(start)                          # after start node is found, we append start node to the list
            path.reverse()                              # we reverse the whole path back, which it will return to normal (start to end) 
            break                                       # then break out of the loop

        for m in graph[node]:                           # for all neighbours of current node
            if m not in graph.keys(): continue          # if the neighbour is not part of the graph.keys or start, continue or skip it
            weight = distn[(node, m)]                   # weight is the distance from current node to its neighbours
            if m not in queue and m not in visited:     # if neighbour not in both queue and visited
                queue.append(m)                         # add to queue and mark node as its parent
                prev_nodes[m] = node
                distt[m] = distt[node] + weight         # dist from neighbour to start is dist from node to start plus neighbour's weight
            elif m in queue and m!= node:               # neighbour is in queue and not the node itself
                if distt[m] > distt[node] + weight:     # check if it's quicker to visit the node or m
                    distt[m] = distt[node] + weight     # update the distance for m and also the parent
                    prev_nodes[m] = node
        
        if node in queue:                               
            queue.remove(node)                          # remove the node from queue
        visited.append(node)                            # and add it to visited
    visited.append(end)                                 # when node is endnode, it doesn't run until the end (leads to endnode not appended)
           
    return path, totaldist, len(visited)
    raise NotImplementedError("To be implemented")
    # End your code (Part 3)

if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')