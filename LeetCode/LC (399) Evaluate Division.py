from collections import deque


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}
        for point, value in zip(equations, values):
            # a에서 b로 가는데 가중치가 value.
            graph[point[0]] = graph.get(point[0], []) + [[point[1], value]]
            # b에서 a로 가는데 가중치는 1/value.
            graph[point[1]] = graph.get(point[1], []) + [[point[0], 1/value]]

        ret = []
        while queries:
            s, e = queries.pop(0)  # s,e는 start, end를 뜻함.
            if s not in graph or e not in graph:  # 둘중 하나라도 graph에 없으면 도달할수 없다는 뜻이므로 -1
                ret.append(-1.0)
                continue
            elif s == e:  # 같으면 1.0
                ret.append(1.0)
                continue

            queue = deque([[s, 1.0]])
            visited = set([s])
            find = False
            while queue:
                node, cur_value = queue.popleft()
                if node == e:  # 이웃들을 들러들러 end에 도달했으면 성공인 경우
                    ret.append(cur_value)
                    find = True
                    break

                for neighbor, value in graph[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append([neighbor, cur_value * value])
            if not find:
                ret.append(-1.0)
        return ret
