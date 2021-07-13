stick_size = 64
stick_stack = [stick_size // 2]
x = int(input())

if x == 64:
    pass
elif stick_size > x:
    while stick_stack[-1] != 1:
        st = stick_stack.pop()
        stick_stack.append(st)
        stick_stack.append(st // 2)
cnt = 0
for i in range(len(stick_stack)):
    if stick_size == 0:
        break
    else:
        if stick_stack[i] <= x:
            cnt += 1
            x -= stick_stack[i]

print(cnt)
