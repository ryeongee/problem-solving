def dense_arr(e1, e2):
    arr = []
    ele1 = min(e1,e2)
    ele2 = max(e1,e2)
    while True:
        if not ele2/ele1<=2:
            arr.append((ele2+1)//2)
            ele2 = (ele2+1)//2
        else:
            break
    return arr

cnt = int(input())
for c in range(cnt):
    n = int(input())
    array = list(map(int,input().split()))
    sum =0
    for i in range(n-1):
        arr = dense_arr(array[i],array[i+1])
        sum +=len(arr)
    print(sum)
