# https://www.acmicpc.net/problem/1475
n = input()
set = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in range(len(n)):
    if n[i] in ['6','9']:
        set['6'] += 1
    else:
        set[n[i]] += 1
if set['6'] % 2 == 0:
    set['6'] = set['6'] // 2
else:
    set['6'] = set['6'] // 2 + 1
print(max(set.values()))
