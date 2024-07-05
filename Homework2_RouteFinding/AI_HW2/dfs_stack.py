import csv
edgeFile = 'edges.csv'
from bfs import *                                       # graphfunc() from 'bfs.py' is used in line 7

def dfs(start, end):
    # Begin your code (Part 2)
    graph, distn, slimit = graphfunc(edgeFile)
    visited = []                                        # list to keep track of node that has been visited
    stack = []                                          # we use stack for depth-first search
    prev_node = {}                                      # to find the parent node (helps with finding the path)
    
    stack.append(start)                                 # start by appending start node to both visited and stack
    visited.append(start)

    # traversing process (iterative): (exploring layer by layer) 
    while stack:                                        # while stack is not empty
        # pop vertex from start to visit next
        # vertex = stack[-1]
        vertex = stack.pop()                            # stack pop from last node which is first in last out
        if vertex not in visited: visited.append(vertex)# we append the vertex to visited here instead
        if vertex not in graph.keys(): continue         # if the vertex is not the start node, skip it or continue
            # # bisa buat hasil recursive:
            # for neighbour in reversed(graph[vertex]):
            # hasil stack:
        for neighbour in graph[vertex]:                 # for all the adjacent nodes of vertex (which is neighbour here)
            if neighbour not in visited:                # if the neighbour has not been visited yet
                prev_node[neighbour] = vertex               # keep track of the parents of the node
                if end in visited:                          # if end is visited
                    while stack:  
                        stack.pop()                                 # pop until the stack is empty
                    # biar krg satu jg
                    visited.pop(-1)                             # pop the current last node of visited
                    break                                   # break out of the for loop
                stack.append(neighbour)                     # only append to stack, unlike bfs to both queue and visited

    # to find the path taken, we use backtrack (from end node to start node)
    path = []                                           # initialize path as list
    node = end                                          # let node be the end node 
    while node != start:                                # so while the node is not start node yet, it will
        path.append(node)                                   # append the node to path list
        node = prev_node[node]                              # and backtrack to previous nodes
    path.append(start)                                  # after start node is found, we append start node to the list
    path.reverse()                                      # we reverse the whole path back, which it will return to normal (start to end)      

    # to find the total distance of the path taken
    totaldist = 0  
    # zip returns zip object(an iterator of tuples)
    # path[:-1] means all the sequence except the last 
    # and path[:1] instead is all sequence except the first    
    for i, j in zip(path[:-1], path[1:]):               # so the path pairs by taking (first, second) until (n-1, n) for (i, j) as distance between i and j
        if (i, j) in distn.keys():                  
            totaldist += distn[(i,j)]                   # add all the distances between (firstnode, secondnode) until the end node

    return path, totaldist, len(visited)

    raise NotImplementedError("To be implemented")
    # End your code (Part 2)

if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')