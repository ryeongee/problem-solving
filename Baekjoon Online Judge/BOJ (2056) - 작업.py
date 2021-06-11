#https://www.acmicpc.net/problem/2056
#동적계획법 1.
def init():
    import sys
    ipt = sys.stdin.readline
    n = int(ipt())
    adj_list = [[0,[]] for i in range(n+1)]
    dp = [0] * (n+1)
    for i in range(1, n+1):
        temp_list = list(map(int, ipt().split()))
        adj_list[i][0] = temp_list[0]
        adj_list[i][1] = temp_list[2:]
        if not temp_list[1]:
            dp[i] = temp_list[0]
    return n, adj_list, dp


n, adj_list, dp = init()
for i in range(1, n+1):
    time, prev_list = adj_list[i]
    if not prev_list:
        continue
    max_time = float('-inf')
    for prev in prev_list:
        max_time = max(max_time, dp[prev])
    dp[i] = time + max_time
print(max(dp))
