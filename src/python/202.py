def isHappy(n: int) -> bool:
    def get_digits(p):
        for d in str(p):
            yield int(d)
    store = set()
    digits = get_digits(n)
    s = 0
    for num in digits:
        s += num * num
    while s not in store:
        if s == 1:
            return True
        store.add(s)
        digits = get_digits(s)
        s = 0
        for num in digits:
            s += num * num
    return False



def main():
    print(isHappy(19))


if __name__ == "__main__":
    main()
