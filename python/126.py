from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff_one(s, k):
            return sum(map(lambda t: t[0] != t[1], zip(s, k))) == 1

        visited = {beginWord}
        layer = {beginWord}
        previous = {beginWord: None}

        if endWord not in wordList:
            return []

        while layer and endWord not in layer:
            new_layer = set()
            for s in layer:
                for w in wordList:
                    if w not in visited and w not in layer and diff_one(w, s):
                        previous.setdefault(w, set()).add(s)
                        new_layer.add(w)

                for v in layer:
                    visited.add(v)
            layer = new_layer

        if endWord not in layer:
            return []

        all_paths = []
        path = [endWord]

        def backtrack(previous_nodes):
            nonlocal all_paths, path

            if previous_nodes is None:
                all_paths.append(path[::-1])
                return

            for n in previous_nodes:
                path.append(n)
                backtrack(previous[n])
                path.pop()

        backtrack(previous[endWord])

        return all_paths


def test():
    s = Solution()

    assert s.findLadders(
        beginWord="hit",
        endWord="cog",
        wordList=["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    ) == [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]

    assert s.findLadders(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log"]
    ) == []

    assert s.findLadders(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "hoy", "coy", "cog"]
    ) == [['hit', 'hot', 'hoy', 'coy', 'cog']]

    print(s.findLadders(
        beginWord="qa",
        endWord="sq",
        wordList=["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                  "ci", "ca",
                  "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
                  "rn", "au",
                  "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh",
                  "co", "ga",
                  "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la",
                  "st", "er",
                  "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr",
                  "sq", "ye"]
    ))

    assert s.findLadders(
        beginWord="hot",
        endWord="dog",
        wordList=["hot", "dog"]
    ) == []


if __name__ == '__main__':
    test()
