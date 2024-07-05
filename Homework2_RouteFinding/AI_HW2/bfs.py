import csv
edgeFile = 'edges.csv'

# to access the value from the file edges.csv  
def graphfunc(efile):                       # can be used in other file
    graph={}                                # dictionary to store a start node and its adjacent or end nodes
    distn={}                                # dictionary to store distance between two nodes
    slimit={}                               # dictionary to store the speed limit between two nodes
    with open(efile, 'r') as file:          # open and read the edges.csv file
        filereader = csv.reader(file)       # read the program using the csv library (csv.reader)
        rows = list(filereader)             # put result of the reader to list row
        for i in range(1,len(rows)):
            startnode = int(rows[i][0])     # to access the startnode of each row
            endnode = int(rows[i][1]) 
            distance = float(rows[i][2])
            speedlimit = float(rows[1][3])

            # if the startnode is not inside the graph, initialize the list and append the endnode
            # if the startnode is already inside the graph, just append the endnode to its list
            if startnode not in graph.keys():
                graph[startnode] = [] 
                graph[startnode].append(endnode)
            else:
                graph[startnode].append(endnode)        

            # the same goes for distn and slimit
            if startnode not in distn.keys():
                distn[(startnode, endnode)] = distance              #key as tuple (a,b)
            if startnode not in slimit.keys():
                slimit[(startnode, endnode)] = speedlimit           #key as tuple (a,b)

    return graph, distn, slimit

def bfs(start, end):
    # Begin your code (Part 1)
    # I started by finding the number of visited nodes to the path then lastly is the distance (visited -> path -> dist)
    graph, distn, slimit = graphfunc(edgeFile)
    
    visited = []                                    # list to keep track of node that has been visited
    queue = []                                      # we use queue for breadth-first search
    prev_node = {}                                  # to find the parent node (helps with finding the path)
    
    visited.append(start)                           # start by appending start node to both visited and queue
    queue.append(start)

    # traversing process: (exploring layer by layer)
    while queue:                                    # while queue is not empty
        x = queue.pop(0)                            # queue.pop(0) is removing the first value in the queue
        if x not in graph.keys(): continue          # means that it does not have any neighbour alr, so we skip it or continue
        for neighbour in graph[x]:                  # for all the adjacent nodes of x (which is neighbour here)
            if neighbour not in visited:            # if neighbour has not been visited yet
                prev_node[neighbour] = x                # keep track of the parents of the node
                if end in visited:                      # if end is visited 
                    while queue:                            
                        queue.pop()                             # pop until the whole queue is empty
                    # biar krg satu
                    visited.pop(-1)                         # pop the current last node of visited
                    break                               # break out of the for loop
                visited.append(neighbour)               # append the neighbour to both visited and queue again
                queue.append(neighbour)                 # so we get to run through the whole graph by bfs

    # to find the path taken, we use backtrack (from end node to start node)
    path = []                                       # initialize path as list
    node = end                                      # let node be the end node 
    while node != start:                            # so while the node is not start node yet, it will
        path.append(node)                               # append the node to path list
        node = prev_node[node]                          # and backtrack to previous nodes
    path.append(start)                              # after start node is found, we append start node to the list
    path.reverse()                                  # we reverse the whole path back, which it will return to normal (start to end)
    # path = [node for node in reversed(path)]      # same as previous line (in more complicated way)

    # to find the total distance of the path taken
    totaldist = 0  
    # zip returns zip object(an iterator of tuples)
    # path[:-1] means all the sequence except the last 
    # and path[:1] instead is all sequence except the first    
    for i, j in zip(path[:-1], path[1:]):           # so the path pairs by taking (first, second) until (n-1, n) for (i, j) as distance between i and j
        if (i, j) in distn.keys():                  
            totaldist += distn[(i,j)]               # add all the distances between (firstnode, secondnode) until the end node
   
    return path, totaldist, len(visited) 
    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)

if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396) #the location
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')