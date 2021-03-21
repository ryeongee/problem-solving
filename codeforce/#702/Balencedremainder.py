t = int(input())
for t in range(t):
    n = int(input())
    a = map(int,input().split())
    while True:
        c = [0,0,0]
        for i in range(n):
            if a[i]%2 == 0:
                c[2]+=1
            if a[i]%1 == 0:
                c[1]+=1
            if a[i]%0 == 0:
                c[0]+=1
        if c[0] == c[1] and c[1] == c[2]:
            break
        else:
            max = max(c[0],c[1],c[2])
            if max == c[0]:
                array
            if max == c[1]:
                pass
            if max == c[2]:
                pass
