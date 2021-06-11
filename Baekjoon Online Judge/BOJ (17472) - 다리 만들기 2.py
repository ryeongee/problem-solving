#https://www.acmicpc.net/problem/17472
#BFS 1.
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, isl_num):
    q.append([x, y])
    isl_num_map[x][y] = isl_num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and isl_num_map[nx][ny] == -1:
                if a[nx][ny]:
                    isl_num_map[nx][ny] = isl_num
                    q.append([nx, ny])


def dfs(x, y, dir, bridge_dis, start):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < n or not 0 <= ny < m:
        return
    if a[nx][ny] == 1:
        end = isl_num_map[nx][ny]
        if start == end:
            return
        if bridge_dis == 1:
            return
        else:
            isl_min_dis[start][end] = min(bridge_dis, isl_min_dis[start][end])
            return
    bridge_dis += 1
    dfs(nx, ny, dir, bridge_dis, start)


def find_min(cnt, index, end):
    global min_ans
    if cnt == end:
        q = deque()
        c = [0 for _ in range(isl_num)]
        isl_cnt, bridge_length = 1, 0
        for i in range(isl_num):
            if not c[i]:
                q.append(i)
                c[i] = 1
                while q:
                    x = q.popleft()
                    for nx in i2i[x]:
                        if select[i2i_bridge[x][nx]] and not c[nx]:
                            c[nx] = 1
                            q.append(nx)
                            isl_cnt += 1
                            bridge_length += isl_min_dis[x][nx]

        if isl_cnt == isl_num:
            min_ans = min(min_ans, bridge_length)
        return

    for i in range(index, bridge_num):
        select[i] = 1
        find_min(cnt+1, i+1, end)
        select[i] = 0


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
isl_num_map = [[-1]*m for _ in range(n)]

isl_num = 0
for i in range(n):
    for j in range(m):
        if a[i][j] and isl_num_map[i][j] == -1:
            bfs(i, j, isl_num)
            isl_num += 1

isl_min_dis = [[10]*isl_num for _ in range(isl_num)]
for i in range(n):
    for j in range(m):
        if a[i][j]:
            for k in range(4):
                dfs(i, j, k, 0, isl_num_map[i][j])

i2i_bridge = [[-1]*isl_num for _ in range(isl_num)]
i2i = [[] for _ in range(isl_num)]
bridge_num = 0
for i in range(isl_num-1):
    for j in range(i+1, isl_num):
        if isl_min_dis[i][j] < 10:
            i2i_bridge[i][j] = bridge_num
            i2i_bridge[j][i] = bridge_num
            i2i[i].append(j)
            i2i[j].append(i)
            bridge_num += 1

select = [0 for _ in range(bridge_num)]
if isl_num % 2 == 0:
    start = isl_num // 2
else:
    start = (isl_num // 2) + 1
min_ans = sys.maxsize
for i in range(start, bridge_num+1):
    find_min(0, 0, i)

if min_ans == sys.maxsize:
    print(-1)
else:
    print(min_ans)
