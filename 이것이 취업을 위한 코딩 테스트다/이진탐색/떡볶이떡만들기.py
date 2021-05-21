n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

start = 0
end = arr[n-1]
mid = (start+end)//2
while start<=end:
    for x in arr:
        mid = (set+end)//2
        if x>mid:
            start = mid +1
        else:
            result = mid
            end  = mid -1
