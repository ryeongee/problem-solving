from collections import defaultdict


def groupWordsF(words):
    grouper = {}
    for word in words:
        length = len(word)
        if length not in grouper:  # 해당 dic에 대해 list 선언 해줘야함
            grouper[length] = []
        grouper[length].append(word)
    return grouper


def groupWordsS(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper


words = ["a", "abcd", "ss", "sadfsafasdf", "sadfsd", "b", "sa"]

print(groupWordsF(words))
print(groupWordsS(words))
