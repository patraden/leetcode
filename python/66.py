from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = True
        i = len(digits) - 1
        while inc and i > -1:
            digits[i] = (digits[i] + 1) % 10
            inc = digits[i] == 0
            i -= 1
        return ([1] + digits) if inc else digits


def main():
    print(Solution().plusOne([9]))


if __name__ == "__main__":
    main()
