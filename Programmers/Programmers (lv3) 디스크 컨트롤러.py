# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    answer = 0
    pop_cnt = sum_t = now = 0
    start = -1
    heap = list()
    while(pop_cnt < len(jobs)):
        for wait_time, process_time in jobs:
            if(start < wait_time <= now):
                heapq.heappush(heap, [process_time, wait_time])
        if(len(heap) > 0):
            current = heapq.heappop(heap)
            pop_cnt += 1
            start = now
            now += current[0]
            sum_t += now - current[1]
        else:
            now += 1
    answer = int(sum_t/len(jobs))
    return answer


solution([[1, 9], [0, 3], [2, 6]])
