def func1(lst):
    answer = [1, 1, 2, 2, 2, 8]
    ans_lst = [0, 0, 0, 0, 0, 0]
    for i in range(len(lst)):
        if answer[i] == lst[i]:
            ans_lst[i] = 0
        else:
            ans_lst[i] = answer[i] - lst[i]
    return map(str, ans_lst)


def main():
    input_lst = list(map(int, input().split(" ")))
    print(" ".join(func1(input_lst)))


main()
