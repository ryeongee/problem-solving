arr = list(input())
stack = []
for i in range(len(arr)):
    if ord(arr[i]) >90:
        arr[i] = chr(ord(arr[i]) - 32)
    if i == 0:
        stack.append(ord(arr[i]))
    if ord(arr[i]) in stack:
        pass
    else:
        stack.append(ord(arr[i]))
maximum = -1
for s in stack:
    count = 0
    for i in range(len(arr)):
        if ord(arr[i]) == s:
            count += 1
    if count == maximum and count != 0:
        sol = "?"
    if count > maximum:
        maximum = count
        sol = chr(s)
print(sol)
