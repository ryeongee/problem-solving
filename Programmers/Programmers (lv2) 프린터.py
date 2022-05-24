def solution(priorities, location):
    answer = 0
    queue = priorities
    ptr = location
    while(queue):
        flag = False
        j = queue.pop(0)
        ptr -= 1

        if (ptr == -1):
            ptr = len(queue)
        for ele in queue:
            if(ele > j):
                queue.append(j)
                flag = True
                break
        if(flag is False):
            answer += 1
            if(ptr == len(queue)):
                break
    return answer


solution([2, 1, 3, 2], 2)
