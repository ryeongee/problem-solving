N, K = map(int, input().split())

table_list = list(range(1, N + 1))
josephus_list = []
pointer = 0
step = K - 1
while len(table_list):
    pointer = (pointer + step) % len(table_list)
    josephus_list.append(str(table_list.pop(pointer)))

print('<' + ', '.join(josephus_list) + '>')
