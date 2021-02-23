import sys
n = int(sys.readline().rstrip())
n_arr = list(map(int,sys.readline().rstrip().split()))

m = int(sys.readline().rstrip())
m_arr = list(map(int,sys.readline().rstrip().split()))
m_arr.sort()

for item in m_arr:
    half = arr[n-1]//2
    while start>= end:
        if half == item:
            return print("yes")
        elif half < item:
            pass
        else:
            pass
