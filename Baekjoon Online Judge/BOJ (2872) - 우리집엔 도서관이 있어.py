#https://www.acmicpc.net/problem/2872
import sys
N = int(sys.stdin.readline())
bks = []
cnt = 0
for _ in range(N):
    bks.append(int(sys.stdin.readline()))

_max = bks[0]

for i in range(1,N):
    if _max < bks[i]:
        if _max+1 != bks[i]:
            cnt+=1
        _max = bks[i]
    else:
        cnt+=1

print(cnt)