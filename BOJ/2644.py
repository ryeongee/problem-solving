"""
https://www.acmicpc.net/problem/2644
"""
# 촌수계산
from collections import deque

n = int(input()) #node's num
f1,f2 = map(int, input().split())
m = int(input()) #edge's num
graph = [[] for _ in range(n+1)]
for i in range(1,m+1):
    node1,node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

result = [0 for i in range(n+1)]
# result 리스트에 각 위치에 도달하면 나오는값 저장 그 값이 0이면 -1 아니면 출력
def bfs(start):
    visited = [0] * (n+1)
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[v]+1
                queue.append(i)

bfs(f1)
print(result[f2] if result[f2] != 0 else -1)
