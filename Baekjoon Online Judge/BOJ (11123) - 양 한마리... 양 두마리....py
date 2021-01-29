#양한마리
import sys
sys.setrecursionlimit(10**6)
T = int(input())
def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == "#" :
        graph[x][y] = 1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True
    return False
result = []
for item in range(T):
    N,M = map(int,input().split())
    graph = [list(input()) for _ in range(N)]
    result.append(0)
    for i in range(N):
        for j in range(M):
            if DFS(i,j) == True:
                result[item] += 1
for item in result:
    print(item)
