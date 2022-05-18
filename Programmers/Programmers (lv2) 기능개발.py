def solution(progresses, speeds):
    answer = []
    new_arr = []
    n = len(progresses)
    # make new arr
    for i in range(n):
        remain_work = 100-progresses[i]
        if remain_work % speeds[i] == 0:
            new_arr.append(remain_work // speeds[i])
        else:
            new_arr.append((remain_work // speeds[i]) + 1)
    cnt = 1
    key = 0
    for j in range(n):
        if(cnt == 1):
            key = new_arr[j]
        if(j == n - 1):
            answer.append(cnt)
        else:
            if key < new_arr[j + 1]:
                answer.append(cnt)
                cnt = 1
            else:
                cnt += 1
    return answer


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
