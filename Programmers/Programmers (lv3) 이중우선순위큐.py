from collections import deque


def solution(operations):
    answer = []
    lst = []
    for operation in operations:
        if len(lst) < 1:
            if operation.split()[0] == "I":
                op, x = operation.split()
                lst.append(int(x))
        else:
            if operation == "D 1":
                lst.remove(max(lst))
            if operation == "D -1":
                lst.remove(min(lst))
            if operation.split()[0] == "I":
                op, x = operation.split()
                lst.append(int(x))
    if len(lst) == 0:
        lst = [0]
    answer = [max(lst), min(lst)]
    return answer


print(solution(["I 16", "D 1"]))
