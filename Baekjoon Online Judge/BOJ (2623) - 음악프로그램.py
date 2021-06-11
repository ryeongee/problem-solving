# https://www.acmicpc.net/problem/2623
#위상정렬 1.
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]

for i in range(M):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]):
        arr[temp[j]].append(temp[j + 1])
        indegree[temp[j + 1]] += 1

result = []
queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while len(queue):
    temp = queue.popleft()
    result.append(temp)

    for second in arr[temp]:
        indegree[second] -= 1
        if indegree[second] == 0:
            queue.append(second)

if len(result) == N:
    for element in result:
        print(element)
else:
    print(0)
