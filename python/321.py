from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n, m = len(nums1), len(nums2)
        nums1_right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums1[stack[-1]] <= nums1[i]:
                stack.pop()
            if stack:
                nums1_right[i] = stack[-1]
            stack.append(i)

        nums2_right = [m] * m
        stack = []
        for i in range(m - 1, -1, -1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            if stack:
                nums2_right[i] = stack[-1]
            stack.append(i)

        print("nums1", nums1)
        print("nums2", nums2)
        print("=" * 20)
        print(nums1_right)
        print(nums2_right)
        print("=" * 20)

        res = []
        i = j = 0
        while len(res) < k:
            if i < n and nums1[i] == 9:
                res.append(nums1[i])
                i += 1
            elif j < m and nums2[j] == 9:
                res.append(nums2[j])
                j += 1
            elif i < n and j < m:
                if nums1[i] == nums2[j]:
                    pass
                elif nums1[i] < nums2[j]:
                    if (n + m - nums1_right[i] - j) >= k - len(res) and nums1_right[i] < n:
                        i = nums1_right[i]
                    else:
                        res.append(nums2[j])
                        j += 1
                else:
                    if (n + m - i - nums2_right[j]) >= k - len(res) and nums2_right[j] < m:
                        j = nums2_right[j]
                    else:
                        res.append(nums1[i])
                        i += 1
            elif i < n:
                if (n - nums1_right[i]) >= k - len(res) and nums1_right[i] < n:
                    i = nums1_right[i]
                else:
                    res.append(nums1[i])
                    i += 1
            elif j < m:
                if (m - nums2_right[j]) >= k - len(res) and nums2_right[j] < m:
                    j = nums2_right[j]
                else:
                    res.append(nums2[j])
                    j += 1
        print(res)


def main():
    # nums1 = [3, 4, 6, 5]
    # nums2 = [9, 1, 2, 5, 8, 3]
    # k = 5
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    Solution().maxNumber(nums1, nums2, k)


if __name__ == "__main__":
    main()
