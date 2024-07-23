class Trie:
    class Node:
        def __init__(self):
            self.alphabet = {}
            self.terminal = False

    def __init__(self):
        self.node = self.Node()

    def insert(self, word: str) -> None:
        node = self.node
        for c in word:
            node = node.alphabet.setdefault(c, self.Node())
        node.terminal = True

    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            if c not in node.alphabet:
                return False
            node = node.alphabet[c]
        return node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            if c not in node.alphabet:
                return False
            node = node.alphabet[c]
        return True


def test():
    t = Trie()
    t.insert('apple')
    print(t.search('apple'))
    print(t.search('app'))
    print(t.startsWith('app'))
    t.insert('app')
    print(t.search('apple'))
    print(t.search('app'))
    print(t.startsWith('app'))


if __name__ == '__main__':
    test()
