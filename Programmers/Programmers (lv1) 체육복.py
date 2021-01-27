def solution(n, lost, reserve):
    count = 0
    complete = [0]*n
    for i in range(0,n):
        for lost_item in lost:
            if i+1 == lost_item:
                complete[i] -= 1
        for reserve_item in reserve:
            if i+1 == reserve_item:
                complete[i] += 1
        complete[i] += 1
    for lost_item in lost:
        for i in range(len(complete)):
            if complete[i] == 2:
                if i != 0 and complete[i-1] == 0 and i+1 == lost_item +1:
                    complete[i] -= 1
                    complete[i-1] +=1
                elif i< len(complete)-1 and complete[i+1] == 0 and (i+1 == lost_item -1):
                    complete[i] -= 1
                    complete[i+1] +=1
    for i in range(len(complete)):
            if complete[i]>0:
                count+=1
    return count
