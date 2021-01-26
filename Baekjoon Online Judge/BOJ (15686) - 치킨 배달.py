from itertools import combinations
N,M = map(int,input().split())
city = [] 
for i in range(N):
    item = list(map(int,input().split()))
    city.append(list(item))

def main():
    return solution(N,M,city)

def solution(N,M,city):
    house, chicken = [],[]
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append([i+1,j+1])
            if city[i][j] == 2:
                chicken.append([i+1,j+1])

    r = len(chicken)
    c_comb = list(combinations(chicken, M))
    sol = list()
    for c_stack in c_comb:
        sum_ = 0
        for h in house:
            minimum = 100
            for c in c_stack:
               c = list(c)
               if abs(h[0]-c[0]) + abs(h[1]-c[1]) < minimum:
                   minimum = abs(h[0]-c[0]) + abs(h[1]-c[1])
            sum_ += minimum
        sol.append(sum_)
    return min(sol)

print(main())
