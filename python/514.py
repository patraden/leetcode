class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, dp = len(ring), {'-1': {0: 0}}
        for i, c in enumerate(ring):
            dp.setdefault(c, {})[i] = 0

        pk = '-1'
        for k in key:
            for i in dp[k]:
                dst = float('inf')
                for j, val in dp[pk].items():
                    dst = min(dst, val + min((i - j) % n, (j - i) % n))
                dp[k][i] = dst + 1
            pk = k

        return min(dp[key[-1]].values())


def test():
    # Solution().findRotateSteps(ring="godding", key="gd")
    print(Solution().findRotateSteps(ring="godding", key="godding"))
    print(Solution().findRotateSteps(ring="zd", key="zd"))


if __name__ == '__main__':
    test()
