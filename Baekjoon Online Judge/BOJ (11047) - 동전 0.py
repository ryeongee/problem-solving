x = input().split(" ") #갯수
x = list(map(int,x))
N, value = x[0], x[1]
item = []
count = 0
for i in range(N):
    item.append(int(input()))

for i in range(N-1,-1,-1): # 큰 단위의 동전 부터 나누기 위해 배열 역순으로
    if value//item[i] > 0: # 현재 금액에 나눌 수 있는 동전이면
        count += value//item[i]
        value = value%item[i]

    if value == 0:
        break
print(count)
