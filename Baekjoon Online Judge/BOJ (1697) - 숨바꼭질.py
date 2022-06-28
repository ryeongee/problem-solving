from collections import deque
MAX = 10 ** 5


def bfs(n, k):
    Q = deque([n])
    dist = [0] * (MAX + 1)

    while Q:
        cur = Q.popleft()
        if cur == k:
            print(dist[cur])
            break

        for nx in (cur - 1, cur + 1, cur * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[cur] + 1
                Q.append(nx)


n, k = map(int, input().split())
bfs(n, k)
