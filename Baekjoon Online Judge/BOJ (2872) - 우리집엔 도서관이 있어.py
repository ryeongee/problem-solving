#https://www.acmicpc.net/problem/2872
import sys
n=int(input())
cnt = 0
d = []
for i in range(n):
 d.append(int(sys.stdin.readline()))
max = d[0]
for i in range(1,n) :
 if d[i] > max :
   if max+1 != d[i] :
     cnt +=1
   max = d[i]
 else :
   cnt +=1
print(cnt)
