def solution(genres, plays):
    answer = []
    idx_lst = []
    for i in range(len(genres)):
        idx_lst.append([i, genres[i], plays[i]])
    # 큰 값 순으로 idx_lst 정렬
    idx_lst = sorted(idx_lst, key=lambda x: (x[1], -x[2], x[0]))
    # 1
    tot_genre_dic = {}
    for g in idx_lst:
        if g[1] not in tot_genre_dic:
            tot_genre_dic[g[1]] = g[2]
        else:
            tot_genre_dic[g[1]] += g[2]
    # .items {key, value} -> [(key, value)]
    tot_genre_dic = sorted(tot_genre_dic.items(),
                           key=lambda x: -x[1])
    # 2
    for td_item in tot_genre_dic:
        cnt = 0
        for t_item in idx_lst:
            if(td_item[0] == t_item[1]):
                cnt += 1
                # 3
                if(cnt > 2):
                    break
                else:
                    answer.append(t_item[0])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))
