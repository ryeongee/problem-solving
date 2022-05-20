def sol(l: list):
    answer = 0
    l_stack = []

    for i in range(0, len(l)):
        if l[i] == "{":
            l_stack.append(l[i])
        else:
            if l_stack:
                l_stack.pop()
            else:
                answer += 1
                l_stack.append("{")
    answer += len(l_stack)//2
    return answer


def main():
    lst = []
    while (True):
        lst.append(list(input()))
        if lst[-1][0] == "-":
            break
    for i in range(len(lst)-1):
        print(str(i+1)+".", sol(lst[i]))


if __name__ == "__main__":
    main()
