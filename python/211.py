class Node:
    def __init__(self):
        self.alphabet = {}
        self.terminal = False


class WordDictionary:

    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        node = self.node
        for c in word:
            node = node.alphabet.setdefault(c, Node())
        node.terminal = True

    def search(self, word: str) -> bool:
        stack = [(self.node, 0)]
        while stack:
            s, idx = stack.pop()
            char = word[idx] if idx < len(word) else None
            if char is None:
                if s.terminal:
                    return True
            else:
                for c in s.alphabet:
                    if char == '.' or c == char:
                        stack.append((s.alphabet[c], idx + 1))
        return False


def test():
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    print(d.search("pad"))
    print(d.search("bad"))
    print(d.search(".ad"))
    print(d.search("b.."))


if __name__ == '__main__':
    test()
