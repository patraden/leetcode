class WordDictionary:

    def __init__(self):
        self.node = {}

    def addWord(self, word: str) -> None:
        node = self.node
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = {}

    def search(self, word: str) -> bool:
        stack = [(self.node, 0)]
        while stack:
            node, idx = stack.pop()
            char = word[idx] if idx < len(word) else None
            if char is None and "#" in node:
                return True
            else:
                for c in node:
                    if char == '.' or c == char:
                        stack.append((node[c], idx + 1))
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
