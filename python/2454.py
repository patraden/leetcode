from typing import List


class Solution:
    """
    Intuition
    Next Greater Element canb resolved with one mono stack.
    Could we resolve this problem with mono stack?

    Explanation
    Use two stack s1 and s2.
    Similar to "Next Greater Element"
    s1 stores the index of elements
    that have not found their first greater element.

    s2 stores the index of elements
    that have found their first greater element,
    have not found their second greater element.

    For each a = A[i] in A
    We first compare the a with the tail elements in s2,
    pop all element smaller than a,
    because a is their second greater element.

    Then we compare the a with the tail elements in s1,
    move all elements smaller than a to the tail of s2,
    because a is their first greater element.

    We repeatedly do this for all A[i] and finally return the result.


    Complexity
    All A[i] is pushed in s1 and s2 at most once.
    All A[i] is pushed in s1 and s2 at most once.

    Time O(n)
    Space O(n)
    """
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res, s1, s2 = [-1] * len(nums), [], []
        for i,a in enumerate(nums):
            while s2 and nums[s2[-1]] < a:
                res[s2.pop()] = a
            tmp = []
            while s1 and nums[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res


def main():
    print(Solution().secondGreaterElement(nums=[2, 4, 0, 9, 6]))
    print(Solution().secondGreaterElement(nums=[11, 10, 4, 9, 20, 12, 19, 18, 16, 8]))


if __name__ == "__main__":
    main()
