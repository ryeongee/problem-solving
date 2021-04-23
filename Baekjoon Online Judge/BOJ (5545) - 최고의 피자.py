#price = A+B*k
#cal = C+sigma(Di)
n = int(input())
a,b = map(int, input().split())
c = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
d.sort(reverse = True)
price = a
cal = c
answer = c/a
new_price = price
new_cal = cal
for i in range(n):
    new_price += b
    new_cal += d[i]
    if new_cal/new_price > answer:
        answer = new_cal/new_price
    else:
        break
print(int(answer))
