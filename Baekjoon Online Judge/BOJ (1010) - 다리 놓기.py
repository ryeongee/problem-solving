import math
cnt = int(input())
for i in range(cnt):
    N,M = map(int,input().split())
    result = 1
    print(math.comb(M,N))
