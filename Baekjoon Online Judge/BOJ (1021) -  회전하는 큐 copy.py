from collections import deque as dq


def sol(l: list, n: int, m: int):
    print(l, n, m)
    answer = 0
    sum = 0
    q = dq(i for i in range(1, n+1))
    size = n
    sum += min(size - l[0], l[0])
    print("first sum :", sum)
    for j in range(0, len(l)-1):
        size -= 1
        if l[j] < len(q)/2:
            sum += min(l[j+1] - l[j], size - l[j+1] + l[j])
            answer = min(l[j+1] - l[j], size - l[j+1] + l[j])
        else:
            sum += min(l[j] - l[j+1], size - l[j] + l[j+1])
            answer = min(l[j] - l[j+1], size - l[j] + l[j+1])
        print("now sum :", answer)
    answer = sum
    return answer


def main():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(sol(lst, n, m))


if __name__ == "__main__":
    main()
