def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


#	[70, 50, 80, 50], 100
# [50,50,70,80]
#solution([70, 50, 80, 50], 100)
print(solution([70,50,50, 50, 80, 50], 100))
#20 50 50 80
#505050507080
