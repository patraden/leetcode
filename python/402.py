class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = [int(c) for c in num]
        nums.append(-1)
        stack, n = [], len(nums)
        for i in range(n):
            while stack and stack[-1] > nums[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(nums[i])

        stack.pop()
        res = "".join([str(num) for num in stack]).lstrip("0")
        return res if res else "0"


def main():
    print(Solution().removeKdigits(num="1432219", k=3))
    print(Solution().removeKdigits(num="10200", k=1))
    print(Solution().removeKdigits(num="10", k=2))
    print(Solution().removeKdigits(num="10", k=1))
    print(Solution().removeKdigits(num="19992", k=1))


if __name__ == "__main__":
    main()
