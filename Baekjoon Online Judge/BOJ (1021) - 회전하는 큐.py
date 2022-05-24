from collections import deque as dq


def sol(l: list, n: int, m: int):
    answer = 0
    cnt = 0
    q = dq([i for i in range(1, n+1)])
    for ele in l:
        while(True):
            if q[0] == ele:
                q.popleft()
                break
            else:
                if q.index(ele) < len(q)/2:
                    while q[0] != ele:
                        q.append(q.popleft())
                        cnt += 1
                else:
                    while q[0] != ele:
                        q.appendleft(q.pop())
                        cnt += 1
    return cnt


def main():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(sol(lst, n, m))


if __name__ == "__main__":
    main()
