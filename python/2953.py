from collections import deque


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:

        groups = len(word) // k if (len(word) // k) < 26 else 26
        ans = 0
        q = deque()

        for f in range(1, groups + 1):

            size = k * f
            unique = {}
            sum_k = 0

            #  first window
            for i in range(size):
                unique[word[i]] = unique.get(word[i], 0) + 1
                if unique[word[i]] == k:
                    sum_k += 1
                if unique[word[i]] == k + 1:
                    sum_k -= 1
                if i > 0 and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                    q.append(i)

            if f == sum_k and not q:
                ans += 1

            # sliding now
            for i in range(size, len(word)):
                first, current = word[i - size], word[i]

                unique[first] -= 1
                if unique[first] == k:
                    sum_k += 1
                if unique[first] == k - 1:
                    sum_k -= 1
                if unique[first] == 0:
                    del unique[first]

                unique[current] = unique.get(current, 0) + 1

                if unique[current] == k:
                    sum_k += 1
                if unique[current] == k + 1:
                    sum_k -= 1

                if abs(ord(word[i]) - ord(word[i - 1])) > 2:
                    q.append(i)
                if q and q[0] <= i - size + 1:
                    q.popleft()

                if f == sum_k and not q:
                    ans += 1

            q.clear()
        return ans


def test():
    print(Solution().countCompleteSubstrings(word="aaabbbccc", k=3))
    print(Solution().countCompleteSubstrings(word="igigee", k=2))
    print(Solution().countCompleteSubstrings(word="aaabc", k=1))


if __name__ == '__main__':
    test()
