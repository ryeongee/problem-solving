from collections import defaultdict, deque


def solution(N, road, K):
    dist = defaultdict(list)
    for a, b, c in road:
        dist[a].append((b, c))
        dist[b].append((a, c))
    visited = [0 for _ in range(N+1)]
    deq = deque([(1, 0)])
    visited[1] = 1  # 1 지났으므로 1로 표시
    while deq:  # deq 값이 있으면 끝날때까지 반복 (전체 탐색)
        x, d = deq.popleft()  # deq 의 첫 번째 값 추출 (큐에 있는 값 순차적으로 꺼냄)

        for v, w in dist[x]:  # 그래프에서 x 값에 속하는 원소 v w 추출
            # d + w = 시간 즉 시간이 기준 K시간 보다 낮아야 하고 방문 안했다면 혹은 방문했는데 지금 시간이 더 작은 값이라면
            # 결국 이렇게 되면 K 시간 안에 최소 시간만 저장이 됨
            if d + w <= K and (not visited[v] or d + w <= visited[v]):
                deq.append((v, d + w))  # deq에 시간, 이동 갱신
                visited[v] = d + w  # visited에 현재 방문 시간 저장
    answer = N+1-visited.count(0)
    return answer


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
