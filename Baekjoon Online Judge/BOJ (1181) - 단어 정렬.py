"""input"""
N = int(input())
words = []
for item in range(N):
    words.append(input())
"""solution"""


def sort_order(lst: list) -> list:
    new_lst = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(lst)):
        min_order = 0
        min_value = "zzzzzz"
        words_stack = []
        if lst[i] == alphabet[i]:
            words_stack.append(lst[i])
        if words_stack:
            for j in range(len(words_stack)):
                while True:

        print(lst)
        print(min_value)
        lst.remove(min_value)
        new_lst.append(min_value)


def sort_length(lst: list) -> list:
    new_lst = []
    for i in range(len(lst)):
        shortest_length = 1000
        shortest_value = 0
        for j in range(len(lst)):
            if len(lst[j]) < shortest_length:
                shortest_length = len(lst[j])
                shortest_value = lst[j]
        lst.remove(shortest_value)
        new_lst.append(shortest_value)
    return new_lst


def remove_overlap(lst: list) -> list:
    """remove overlap items in list, and return list"""
    new_set = set(lst)
    return list(new_set)


def print_words(lst: list):
    """prints the items in a list line by line."""
    for ans_item in lst:
        print(ans_item)


def main():
    global words
    ans_words = remove_overlap(words)
    sort_order(ans_words)
    ans_words.sort()
    ans_words = sort_length(ans_words)
    print_words(ans_words)


"""Output"""
main()
