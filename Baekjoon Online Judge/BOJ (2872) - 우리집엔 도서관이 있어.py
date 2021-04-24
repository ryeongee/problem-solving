#https://www.acmicpc.net/problem/2872
ans = []
# def sorting(arr, n):
#     max = 0
#     for i in range(n):
#         if arr[i]> max:
#             max = arr[i]
#     arr = arr[:max-1]
#     # del a[max]
#     sorting(arr, n-1)
#     return ans.append(arr[max])

n = int(input())
books = []
answer = []
for _ in range(n):
    books.append(int(input()))
cnt = 0
while True:
    maximum = max(books)
    del books[maximum]
    if max(books) != item and :
        cnt += 1
