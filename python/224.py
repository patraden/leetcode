from string import digits

"""
https://en.wikipedia.org/wiki/Shunting_yard_algorithm
https://habr.com/ru/articles/596925/
"""

class Solution:
    def calculate(self, s: str) -> int:
        priority = {'(': -1, ')': -1, '+': 0, '-': 0, '~': 1}
        res = []
        i = 0
        stack = []
        last_token = None
        while i < len(s):
            if s[i] in digits:
                num = s[i]
                while (i + 1) < len(s) and s[i + 1] in digits:
                    num += s[i + 1]
                    i += 1
                res.append(int(num))
                last_token = num
            elif s[i] == "(":
                stack.append(s[i])
                last_token = s[i]
            elif s[i] == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                assert stack[-1] == "("
                stack.pop()  # removing ")" from stack
                last_token = s[i]
            elif s[i] == "+":
                while stack and priority[stack[-1]] >= priority[s[i]]:
                    res.append(stack.pop())
                stack.append(s[i])
                last_token = s[i]
            elif s[i] == "-":
                while stack and priority[stack[-1]] >= priority[s[i]]:
                    res.append(stack.pop())
                if i == 0 or (i > 0 and last_token and last_token in "+("):  # unary -
                    stack.append("~")
                else:
                    stack.append(s[i])
                last_token = s[i]
            i += 1
        while stack:
            res.append(stack.pop())

        assert not stack
        for elem in res:
            if isinstance(elem, int):
                stack.append(elem)
            elif elem == '~':
                num = stack.pop()
                stack.append(-num)
            elif elem == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif elem == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
        assert stack
        return stack[-1]


def main():
    print(Solution().calculate("(1 + (-3) + (44 + 5 + 222) - 3)"))
    print(Solution().calculate(" 2-1 + 2 "))
    print(Solution().calculate("(1-(4+5+2)-3)+(6+8)"))
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
    print(Solution().calculate("20 -  (20-5) "))


if __name__ == "__main__":
    main()
