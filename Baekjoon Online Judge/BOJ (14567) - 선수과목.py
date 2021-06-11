#https://www.acmicpc.net/problem/14567
#위상정렬 1.
import sys
from collections import deque

def solution():
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    degree = [0] * (N+1)
    time = [0] * (N+1)
    dq = deque()

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        degree[B] += 1

    for i in range(1, N + 1):
        if degree[i] == 0:
            dq.append((i, 1))

    while dq:
        idx, t = dq.popleft()
        time[idx] = t
        for j in graph[idx]:
            degree[j] -= 1

            if degree[j] == 0:
                dq.append((j, t+1))

    for t in range(1, len(time)):
        print(time[t], end=' ')

solution()
