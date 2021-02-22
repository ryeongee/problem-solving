n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start = 0
end = arr[n-1]
mid = (start+end)//2
while start<=end:
    for x in arr:
        if x>mid:
            mid = (set+end)//2
            start -1
        else:
            set
