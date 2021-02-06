num = int(input())
t_list = []
for i in range(num):
    t_list.append(list(map(int,input().split())))
t_list = sorted(t_list, key=lambda a: a[0])
t_list = sorted(t_list, key=lambda a: a[1])
count = 0
list_end = 0
for i, j in t_list:
    if i >= list_end:
        count += 1
        list_end = j
print(count)
