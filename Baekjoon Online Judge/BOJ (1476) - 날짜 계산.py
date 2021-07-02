"""Input"""
E, S, M = map(int, input().split())


def solution(e: int, s: int, m: int) -> int:
    """input E, S, M and counting total day to return the answer"""
    total_cnt, e_cnt, s_cnt, m_cnt = 1, 1, 1, 1
    while True:
        if e_cnt == e and s_cnt == s and m_cnt == m:
            break
        else:
            total_cnt += 1
            e_cnt += 1
            s_cnt += 1
            m_cnt += 1
            if e_cnt == 16:
                e_cnt = 1
            if s_cnt == 29:
                s_cnt = 1
            if m_cnt == 20:
                m_cnt = 1
    return total_cnt


"""Output"""
print(solution(E, S, M))