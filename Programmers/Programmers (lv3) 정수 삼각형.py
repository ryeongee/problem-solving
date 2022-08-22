def TriDP(n, before_answer, triangle):
    answer = []
    b_answer = []
    line = triangle[n]
    for i in range(n+1):
        b_answer.append(max(before_answer[i], before_answer[i+1]))
    for j in range(n+1):
        answer.append(b_answer[j] + line[j])
    if(n == 0):
        return answer[0]
    else:
        return TriDP(n - 1, answer, triangle)

def solution(triangle):
    answer = 0
    n = len(triangle) - 1
    answer = TriDP(n - 1, triangle[n], triangle)
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))