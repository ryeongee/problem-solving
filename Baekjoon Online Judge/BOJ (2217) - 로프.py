#https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline
N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse = True)

for i in range(N):
    rope[i] = rope[i]*(i+1)

print(max(rope))
