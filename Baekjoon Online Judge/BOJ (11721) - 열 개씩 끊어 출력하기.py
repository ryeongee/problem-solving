arr = list(input())
num = len(arr)//10
for i in range(num):
    print(''.join(arr[10*i:10*(i+1)]))
if len(arr)%10 != 0:
    print(''.join(arr[10*(num):]))
