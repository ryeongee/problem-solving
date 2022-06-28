import sys

input = sys.stdin.readline

n, m = map(int, input().split())
p_dic = {}
answer = []
for i in range(n):
    x = input().rstrip()
    if x not in p_dic:
        p_dic[x] = i

for _ in range(m):
    y = input().rstrip()
    if y in p_dic.keys():
        answer.append(y)

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
