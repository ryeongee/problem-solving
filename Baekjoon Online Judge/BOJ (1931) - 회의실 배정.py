N = int(input()) #회의실 갯수
plan = []
count = 0
save = []

for i in range(N):
    item = input().split(" ") # i 번째 회의
    item = list(map(int,item)) # 정수로 변환
    plan.append([item[0], item[1]])  #시작시간, 종료시간
plan.sort() # 오름차순 정렬
save = plan
for i in range(N):
    save.pop(i) #기준 list 제거
    for j in range(1,N-1):
        if plan[i][0]<=plan[i+j][0] and plan[i+1][1]<=plan[i][1]: #범위안에있으면
            save.remove(plan[i+j]) #제거

print(save)
