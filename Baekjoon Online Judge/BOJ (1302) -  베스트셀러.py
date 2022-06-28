
def main():
    n = int(input())
    answer = []
    books_dic = {}
    # books_dic[book, value]
    for _ in range(n):
        book = input()
        if(book not in books_dic):
            books_dic[book] = 1
        else:
            books_dic[book] += 1
    max_val = max(books_dic.values())
    for b, val in books_dic.items():
        if(max_val == val):
            answer.append(b)
    print(sorted(answer)[0])


if __name__ == "__main__":
    main()
