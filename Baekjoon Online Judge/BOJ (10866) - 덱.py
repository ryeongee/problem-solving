from collections import deque


def sol(ord_lst: list):
    answer = 0
    lst = ord_lst
    dq = deque()
    for ord in lst:
        # 명령 2개 일때
        rslt = None
        if len(ord.split()) > 1:
            new_ord, x = ord.split()
            if new_ord == "push_front":
                dq.appendleft(x)
            # push_back
            else:
                dq.append(x)
        else:
            if ord == "pop_front":
                if len(dq) == 0:
                    rslt = -1
                else:
                    rslt = dq.popleft()
            if ord == "pop_back":
                if len(dq) == 0:
                    rslt = -1
                else:
                    rslt = dq.pop()
            if ord == "size":
                rslt = len(dq)
            if ord == "empty":
                rslt = 0
                if len(dq) == 0:
                    rslt = 1
            if ord == "front":
                if len(dq) == 0:
                    rslt = -1
                else:
                    rslt = dq[0]
            if ord == "back":
                if len(dq) == 0:
                    rslt = -1
                else:
                    rslt = dq[-1]
            print(rslt)


def main():
    n = int(input())
    order_list = []
    for _ in range(n):
        order_list.append(input())
    sol(order_list)


if __name__ == "__main__":
    main()
