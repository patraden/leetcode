def generateParenthesis(n: int) -> list[str]:
    res = []

    def brackets_sequence_generate(open_left: int, close_left: int, prefix="") -> None:
        if open_left == close_left == 0:
            res.append(prefix)
            return
        if prefix == "" or open_left == close_left:
            brackets_sequence_generate(open_left - 1, close_left, prefix + "(")
        elif open_left == 0:
            brackets_sequence_generate(open_left, close_left - 1, prefix + ")")
        else:
            brackets_sequence_generate(open_left - 1, close_left, prefix + "(")
            brackets_sequence_generate(open_left, close_left - 1, prefix + ")")
    brackets_sequence_generate(open_left=n, close_left=n)
    return res


def main():
    print(generateParenthesis(1))
    print(generateParenthesis(2))
    print(generateParenthesis(3))
    print(generateParenthesis(4))


if __name__ == "__main__":
    main()
