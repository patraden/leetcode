from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # invariant: left is the smallest between two
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


def test():
    s = Solution()
    print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(s.twoSum(numbers=[2, 3, 4], target=6))
    print(s.twoSum(numbers=[-1, 0], target=-1))
    print(s.twoSum(numbers=[-10, -8, 0, 0, 11], target=3))
    print(s.twoSum(numbers=[-1, -1, 1, 1, 1, 1], target=-2))


if __name__ == '__main__':
    test()
