import csv
import sys
edgeFile = 'edges.csv'
from bfs import *
sys.setrecursionlimit(7000)


def dfs(start, end):
    # Begin your code (Part 2)
    # # (๑•̀ㅂ•́)و✧
    
    raise NotImplementedError("To be implemented")
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')