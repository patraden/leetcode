def lengthOfLongestSubstring(s: str) -> int:
    d = dict()
    res = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i
        else:
            k = d[s[i]]
            d[s[i]] = i
            new_d = dict()
            for key in d:
                if d[key] >= k:
                    new_d[key] = d[key]
            d = new_d
        res = max(res, len(d))
    return res


def main():
    lengthOfLongestSubstring("pwwkew")
    lengthOfLongestSubstring("abcabcbb")
    lengthOfLongestSubstring("bbbbb")
    lengthOfLongestSubstring(" ")
    lengthOfLongestSubstring("au")
    lengthOfLongestSubstring("dvdf")


if __name__ == "__main__":
    main()
