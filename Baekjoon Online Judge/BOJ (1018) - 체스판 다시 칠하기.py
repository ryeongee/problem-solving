"""Input"""
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(input()))
"""Setting answer"""
ans1 = [["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"]]

ans2 = [["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"]]
"""Main"""
min_cnt = 1000
for i in range(N-7):
    for j in range(M-7):
        board2 = [row[j:j + 8] for row in board[i:i + 8]]  # Slicing chess board to 8*8
        cnt1, cnt2 = 0, 0
        for a in range(8):
            for b in range(8):
                if ans1[a][b] != board2[a][b]:
                    cnt1 += 1
                if ans2[a][b] != board2[a][b]:
                    cnt2 += 1
                else:
                    pass
        temp = min(cnt1, cnt2)
        if min_cnt > temp:
            min_cnt = temp
"""Output"""
print(min_cnt)
