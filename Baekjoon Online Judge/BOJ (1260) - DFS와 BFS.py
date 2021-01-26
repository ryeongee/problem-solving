"""
https://www.acmicpc.net/problem/1260
"""
from collections import deque
import sys
sys.setrecursionlimit(10**6)

_n,_e,v = map(int, input().split())
visited_1 = [False]*(1001)
visited_2 = [False]*(1001)
graph = [[] for _ in range(1001)]

for i in range(1,_e+1):
    node1,node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node1].sort()
    graph[node2].append(node1)
    graph[node2].sort()

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
dfs(graph,v,visited_1)
print("")
bfs(graph,v,visited_2)
