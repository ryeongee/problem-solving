n = int(input())
if n>1:
    print(" "*(n-1)+"*")
    if n>2:
        for i in range(1,n-1):
            print(" "*(n-1-i)+"*"+" "*(2*i-1)+"*")
print("*"*(n*2-1))
