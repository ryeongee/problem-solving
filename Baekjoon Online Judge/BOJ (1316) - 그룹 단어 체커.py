count = 0
N = int(input())
for i in range(N):
    array = list(input())
    stack = []
    for i in range(len(array)):
        if i == 0 or (array[i] != stack[-1] and array[i] not in stack):
            stack.append(array[i])
        if array[i] in stack and array[i] != stack[-1]:
            stack = []
            break
    if len(stack) > 0:
        count += 1
print(count)
