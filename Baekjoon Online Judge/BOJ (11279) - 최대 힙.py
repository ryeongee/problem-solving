import heapq
import sys


def main():
    n = int(input())
    max_heap = []
    for _ in range(n):
        item = int(sys.stdin.readline())
        if item != 0:
            heapq.heappush(max_heap, (-item, item))
        else:
            if len(max_heap) == 0:
                print(0)
            else:
                print(heapq.heappop(max_heap)[1])


if __name__ == "__main__":
    main()
