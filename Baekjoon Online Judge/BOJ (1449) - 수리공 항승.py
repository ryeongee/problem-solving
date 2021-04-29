# https://www.acmicpc.net/problem/1449
N, L = map(int,input().split())
loc = list(map(int,input().split()))

st = 0
cnt = 0

for now in loc:
    if st < now:
        st = now+L-1
        cnt+=1

print(cnt)
