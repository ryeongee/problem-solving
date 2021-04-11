# https://www.acmicpc.net/problem/2599
# 6
# 4 2
# 1 3
# 1 1
n = int(input())
stuList = []
menA, womA = stuList.append(list(map(int,input().split())))
menB, womB = stuList.append(list(map(int,input().split())))
menC, womC = stuList.append(list(map(int,input().split())))

def function(lst, n):
    t = [0,0,0]
    ans = [0,[[0,0],[0,0],[0,0]]]
    for col in range(3):
        if col == 0:
            ana = [1,2]
        if col == 1:
            ana = [0,2]
        if col == 2:
            ana = [0,1]
        a = lst[col][0]
        for i in range(lst[0][0]):
            cnt = 0
            for j in ana:
                if lst[j][1] > 0 and a != 0:
                    lst[j][1] -=1
                    a -=1
                    ans[1][[col][cnt]] += 1
                else:
                    break
                    cnt+=1
        if a == 0:
            t[col] = 1
    if t == [1,1,1]:
        ans[0] = 1
    return ans

answer = function(stuList,n)
print(answer)
