# https://www.acmicpc.net/problem/1037

"""Input"""
N = int(input())
lst_divisors = list(map(int, input().split()))


def solution(lst: list) -> int:
    """input list type divisors, get integer N and return N"""
    return min(lst) * max(lst)


answer = solution(lst_divisors)
"""Output"""
print(answer)
