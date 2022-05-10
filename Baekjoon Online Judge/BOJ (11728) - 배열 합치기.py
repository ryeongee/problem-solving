import sys


def sol():
    ans = 0
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = sorted(A+B)

    # output
    print(*ans)


sol()
