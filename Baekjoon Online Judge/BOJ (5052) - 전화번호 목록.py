from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word = False
        self.cnt = 0  # 추가
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.consistency = True  # 추가

    # 단어 삽임
    def insert(self, word: str) -> None:
        if not self.consistency:    # 추가
            return

        node = self.root

        for char in word:
            if not char.isdigit():  # 숫자가 아닌 값 트라이에 넣지 않는다. ex) "123-456"
                continue
            node = node.children[char]
            node.cnt += 1

            if node.word:
                self.consistency = False
                return

        node.word = True  # 단어 마지막 true
        if node.cnt > 1:  # 거꾸로 일때
            self.consistency = False

    def check_consistency(self) -> bool:
        return self.consistency


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        trie = Trie()
        for _ in range(n):
            tel = input()
            trie.insert(tel)
        print(['NO', 'YES'][trie.check_consistency()])


if __name__ == "__main__":
    main()
