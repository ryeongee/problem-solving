import heapq
from typing import List


# 정렬되지 않은 요소에서 k번째 큰 요소를 추출해라


def findKthLargest(nums, k):
    print(heapq.nlargest(k, nums)[-1])
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
    for _ in range(1, k):
        heapq.heappop(heap)
    return -heapq.heappop(heap)


ipt = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
answer = 4

print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
