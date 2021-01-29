"""받아오기"""
N,M = map(int,(input().split()))
board = []
for i in range(N):
    board.append(list(input()))
"""정답설정"""
for i in range(0,8):
    if i%2==0:
       ans1.append("BWBWBWBW")
       ans2.append("WBWBWBWB")#정답이될 체스판
    else:
       ans1.append("WBWBWBWB")
       ans2.append("BWBWBWBW")
c_board = []
s_min = 99999
if N == 8 and M == 8:
    c_ex = board
    result = 0
    for x in range(8):
        stack = [c_ex[x][0]]
        for y in range(1,8):
            if c_ex[x][y] != stack[-1]:
                stack.append(c_ex[x][y])
        result += (8-len(stack)+1)//2
        if result >= s_min:
            break
    if result < s_min:
        s_min = result

elif N == 8:
        for j in range(M-8):
            c_ex = [row[j:j+8] for row in board[:]]
            result = 0
            for x in range(8):
                stack = [c_ex[x][0]]
                for y in range(1,8):
                    if c_ex[x][y] != stack[-1]:
                        stack.append(c_ex[x][y])
                result += (8-len(stack)+1)//2
                if result >= s_min:
                    break
            if result < s_min:
                s_min = result

elif M == 8:
    for i in range(N-8):
            c_ex = [row[:] for row in board[i:i+8]]
            result = 0
            for x in range(8):
                stack = [c_ex[x][0]]
                for y in range(1,8):
                    if c_ex[x][y] != stack[-1]:
                        stack.append(c_ex[x][y])
                result += (8-len(stack)+1)//2
                if result >= s_min:
                    break
            if result < s_min:
                s_min = result

else:
    for i in range(N-8):
        for j in range(M-8):
            c_ex = [row[j:j+8] for row in board[i:i+8]]
            result = 0
            for x in range(8):
                stack = [c_ex[x][0]]
                for y in range(1,8):
                    if c_ex[x][y] != stack[-1]:
                        stack.append(c_ex[x][y])
                result += (8-len(stack))//2
                if result >= s_min:
                    break
            if result < s_min:
                s_min = result
print(s_min)
