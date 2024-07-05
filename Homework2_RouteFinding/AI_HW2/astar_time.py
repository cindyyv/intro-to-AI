import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'
from bfs import *
graph, distn, slimit = graphfunc(edgeFile)
from astar import *
heur1, heur2, heur3 = heurfunc(heuristicFile)

def astar_time(start, end):
    # Begin your code (Part 6)
    # heur1, heur2, heur3 = heurfunc(heuristicFile)

    # # opened: list of nodes which have been visited, but neighbors havent all been inspected,
    # # closed: list of nodes which have been visited and neigbors have been inspected
    # # distt: current distances from start node to all other nodes

    # opened = []
    # closed = []
    # distt = {}
    # prev_nodes = {}

    # opened.append(start)
    # distt[start] = 0
    # prev_nodes[start] = start
    # newpath = []  
    # totaldist = 0
    # while len(opened)>0:
    #     # n = node
    #     node = None
    #     # f(n) = g(n) + h(n)
    #     # g(n): value of shortest path from start node to node n
    #     # h(n): heuristic approx. of the node's value

    #     # find node with lowest value of f(n)
    #     for v in opened:
    #         # print(v, heur1[v][0])
    #         if (start, end) == (2270143902, 1079387396):
    #             if node == None or slimit[(v, )] < distt[node] + heur1[node][0]:
    #                 node = v
    #         elif (start, end) == (426882161, 1737223506):
    #             if node == None or distt[v] + heur2[v][0] < distt[node] + heur2[node][0]:
    #                 node = v
    #         elif (start, end) == (1718165260, 8513026827):
    #             if node == None or distt[v] + heur3[v][0] < distt[node] + heur3[node][0]:
    #                 node = v
        
    #     # path does not exist if n is end
    #     if node == None:                    # ganti ini
    #         break

    #     # if current node is end node, remake a new path from it to start node
    #     if node == end:
    #         totaldist = distt[node]
    #         while prev_nodes[node] != node:
    #             newpath.append(node)
    #             node = prev_nodes[node]
    #         newpath.append(start)
    #         newpath.reverse()
    #         break

    #     # for all neighbors of current node
    #     for m in graph[node]:
    #         if m not in graph.keys(): continue
    #         weight = distn[(node, m)]
    #         if m not in opened and m not in closed:
    #             # add to opened and note node as its parent
    #             opened.append(m)
    #             prev_nodes[m] = node
    #             distt[m] = distt[node] + weight
    #         else:
    #             # check quicker to visit the node or m
    #             # update parent and distt data
    #             if distt[m] > distt[node] + weight:
    #                 distt[m] = distt[node] + weight
    #                 prev_nodes[m] = node
    #                 if m in closed:
    #                     closed.remove(m)
    #                     opened.append(m)
        
    #     if node in opened:          
    #         opened.remove(node)   
    #     closed.append(node)
    # closed.append(end)              
    # return newpath, totaldist, len(closed)

    raise NotImplementedError("To be implemented")
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
