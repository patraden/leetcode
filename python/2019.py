from typing import List, Set
from functools import cache


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        @cache
        def scores(i, j) -> Set[int]:
            if j - i == 1:
                return {int(s[i])}

            res = set()
            for sign_index in range(i + 1, j, 2):
                for num1 in scores(i, sign_index):
                    for num2 in scores(sign_index + 1, j):
                        num = num1 + num2 if s[sign_index] == "+" else num1 * num2
                        if num <= 1000:
                            res.add(num)
            return res

        exact_answer = eval(s)
        good_answers = [num for num in answers if num in scores(0, len(s))]
        return sum([5 if num == exact_answer else 2 for num in good_answers])


def main():
    s = Solution()
    # print(s.scoreOfStudents(s="7+3*1*2", answers=[20, 13, 42]))
    # print(s.scoreOfStudents(s="3+5*2", answers=[13, 0, 10, 13, 13, 16, 16]))
    # print(s.scoreOfStudents(s="6+0*1", answers=[12, 9, 6, 4, 8, 6]))
    # print(s.scoreOfStudents(s="1+2*3+4", answers=[13, 21, 11, 15]))
    print(s.scoreOfStudents(s="9+8*0", answers=[0]))


if __name__ == "__main__":
    main()
