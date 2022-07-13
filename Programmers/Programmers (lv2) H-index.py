def solution(citations):
    citations.sort()
    h = len(citations)
    while True:
        for i, n in enumerate(citations):
            if n >= h and len(citations[i:]) >= h:
                return h
        else:
            h -= 1
            continue
        break
