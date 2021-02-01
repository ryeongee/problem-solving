n = int(input())
total = n
for i in range(1,n+1):
    print(" "*(total - i), end = '')
    print('*'*i)
