def fib_generator():
    prev = 0
    pprev = 0
    if pprev == 0:
        prev = 1
    while True:
        yield prev
        prev, pprev = prev + pprev, prev


if __name__ == "__main__":
    g = fib_generator()
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

