"""
https://www.youtube.com/watch?v=PIeiiceWe_w&t=222s
"""


def pi_func(s):
    """ Prefix function """
    dp = [0] * len(s)
    for i in range(1, len(s)):
        k = dp[i - 1]
        while k > 0 and s[i] != s[k]:
            k = dp[k]
        if s[i] == s[k]:
            k += 1
        dp[i] = k
    return dp


def substring_search(p, s) -> bool:
    pi = pi_func(f"{p}#{s}")
    for i in range(len(p) + 1, len(s)):
        if pi[i] == len(p):
            return True
    return False


decoder = {
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4,
    'j': 5, 'k': 5, 'l': 5,
    'm': 6, 'n': 6, 'o': 6,
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8,
    'w': 9, 'x': 9, 'y': 9, 'z': 9
}


def problem(number, strings):
    def decode(s: str):
        return ''.join(str(decoder[e]) for e in s)

    res = []
    for elem in strings:
        elem = decode(elem)
        res.append(substring_search(elem, str(number)))


if __name__ == "__main__":
    print(substring_search("as", "16723167asd313"))
