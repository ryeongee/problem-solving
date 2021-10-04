# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return True
        
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return False
    return True
tot_num = int(input())
result = [0]*tot_num
for t in range(tot_num):
    N, M, b_num = map(int,input().split())
    graph = [[0 for col in range(M)] for row in range(N)]

    for b in range(b_num):
        dx, dy = map(int,input().split())
        graph[dx][dy] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i,j) == False:
                result[t] += 1
for item in result:
    print(item)
