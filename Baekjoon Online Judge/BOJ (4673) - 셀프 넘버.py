# https://www.acmicpc.net/problem/4673
MAX_N = 10000
answer_lst = list(range(1, MAX_N))


def find_not_self_number(n: int) -> int:
    """input integer n and find not self number and return"""
    ans = n
    if n > 9999:
        ans += n // 10000
        n = n % 10000
    if n > 999:
        ans += n // 1000
        n = n % 1000
    if n > 99:
        ans += n // 100
        n = n % 100
    if n > 9:
        ans += n // 10
        n = n % 10
    if n > 0:
        ans += n
    return ans


def get_self_number(self_numbers: list) -> list:
    """input 1~10000(MAX) list and return self numbers list"""
    for i in range(1, MAX_N):
        not_self_num = find_not_self_number(i)
        if not_self_num in self_numbers:
            self_numbers.remove(not_self_num)
    return self_numbers


def print_self_number(self_numbers: list):
    """input list of self numbers and print numbers one by one"""
    for self_num in self_numbers:
        print(self_num)


print_self_number(get_self_number(answer_lst))
