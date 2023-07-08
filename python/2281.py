from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 1000000007
        n = len(strength)
        stack = []
        left = [(-1, 0)] * n
        dp = [0] * n
        prefix = [0] * (n + 1)
        prefix_acc = [0] * (n + 1)

        for i, num in enumerate(strength):
            prefix_acc[i + 1] = prefix_acc[i] + ((i + 1) * num) % mod

        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % mod

        stack_sum = 0
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                k = stack.pop()
                stack_sum -= strength[k] * (k - (stack[-1] if stack else -1))
            if stack:
                left[i] = (stack[-1], stack_sum)
            stack_sum += strength[i] * (i - (stack[-1] if stack else -1))
            stack.append(i)

        final_res = 0
        for i in range(n):
            #  handling increment from last minimum
            res = 0
            k, s = left[i]
            if k > -1:
                res += (dp[k] + s * (prefix[i + 1] - prefix[k + 1])) % mod

            #  handling everything after last minimum
            res += (
                    (prefix_acc[i + 1] - prefix_acc[k + 1]) -
                    (k + 1) * (prefix[i + 1] - prefix[k + 1])
                   ) * strength[i] % mod
            dp[i] = res
            final_res += dp[i]

        return final_res % mod


def main():
    print(Solution().totalStrength([1, 3, 1, 2]))
    print(Solution().totalStrength([5, 4, 6]))
    print(Solution().totalStrength([5, 6, 12]))  # 483


if __name__ == "__main__":
    main()
