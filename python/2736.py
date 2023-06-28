from typing import List, Tuple


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        #  preparing nums
        nums = sorted(list(zip(nums1, nums2)))
        n = len(nums)
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i][1] >= stack[-1][1] and sum(nums[i]) >= sum(stack[-1]):
                stack.pop()
            if (not stack) or (nums[i][1] > stack[-1][1] and sum(nums[i]) < sum(stack[-1])):
                stack.append(nums[i])
            right[i] = stack.copy()

        #  main algorythm
        m = len(queries)
        res = [None] * m

        for i, (x, y) in enumerate(queries):
            x_index = self.left_most_search(nums, x)
            if x_index == n:
                res[i] = -1
            else:
                y_index = self.left_most_search(right[x_index], y, first=False)
                if y_index == len(right[x_index]):
                    res[i] = -1
                else:
                    res[i] = sum(right[x_index][y_index])
        return res

    def left_most_search(self, nums: List[Tuple[int, int]], target: int, first=True) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if target <= (nums[m][0] if first else nums[m][1]):
                r = m
            else:
                l = m + 1
        return l


def main():
    # nums1, nums2 = [4, 3, 1, 2], [2, 4, 9, 5]
    # queries = [[4, 1], [1, 3], [2, 5]]

    # nums1, nums2 = [3, 2, 5], [2, 3, 4]
    # queries = [[4, 4], [3, 2], [1, 1]]

    # nums1, nums2 = [68], [86]
    # queries = [[85,84], [6,84]]

    # nums1, nums2 = [35, 69], [63, 21]
    # queries = [[59, 93], [20, 8]]

    nums1, nums2 = [59, 94], [44, 86]
    queries = [[57, 34], [26, 94], [40, 97], [70, 78]]
    #  [180,-1,-1,180]

    sol = Solution()
    print(sol.maximumSumQueries(nums1, nums2, queries))


if __name__ == "__main__":
    main()
