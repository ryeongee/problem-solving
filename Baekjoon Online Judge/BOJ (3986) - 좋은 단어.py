from inspect import stack


def sol():
    cnt = 0
    # input
    n = int(input())
    for _ in range(n):
        # input
        arr = input()
        f_stack = []
        for i in range(len(arr)):
            if f_stack and arr[i] == f_stack[-1]:
                f_stack.pop()
            else:
                f_stack.append(arr[i])
        if not f_stack:
            cnt += 1
    print(cnt)


sol()
