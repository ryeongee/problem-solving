"""input"""
N = int(input())
words = []
for item in range(N):
    words.append(input())
"""solution"""


def sort_order(lst: list) -> list:
    pass


def sort_length(lst: list) -> list:
    pass


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
    ans_words.sort()
    ans_words.sort(key=len)
    print_words(ans_words)


"""Output"""
main()
