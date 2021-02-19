m_list = []
n,k = map(int,input().split())
for i in range(n):
    m_list.append(int(input()))
min_item = min(m_list)
max_item = max(m_list)
max = max_item
min = 0
while True:
    count = 0
    half = (min+max)//2
    for item in m_list:
        count += item//half
    if count > k:
        tmp = half
        half = (half+max)//2
        min = tmp-1
    if count < k:
        tmp = half
        half = (half+min)//2
        max = tmp+1
    if count == k:
        break
if half == -1:
    print(0)
else:
    print(half)
