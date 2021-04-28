# https://www.acmicpc.net/problem/13417
T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(str, input().split()))
    my = [cards[0]]
    for i in range(1,N):
        if ord(cards[i]) <= ord(my[0]):
            my.insert(0,cards[i])
        else:
            my.append(cards[i])
    print(''.join(my))
