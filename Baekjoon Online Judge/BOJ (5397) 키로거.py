from matplotlib import collections


import collections
test_cases = int(input())

for _ in range(test_cases):
    left = []
    right = []
    pwd = input()
    right = collections.deque()
    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop())
        elif x == "<":
            if left:
                right.append(left.pop())
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)

print("".join(left)+"".join(reversed(right)))
