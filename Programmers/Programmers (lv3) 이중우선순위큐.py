import heapq


def solution(operations):
    heap = []
    max_heap = []
    for operation in operations:
        cur = operation.split()
        if cur[0] == "I":
            num = int(cur[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            if len(heap) == 0:
                pass
            elif cur[1] == "1":
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif cur[1] == "-1":
                min_value = heapq.heappop(heap)
                max_heap.remove((-min_value, min_value))

    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    return answer


print(solution(["I 16", "D 1"]))
