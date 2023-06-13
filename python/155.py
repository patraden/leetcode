class MinStack:

    def __init__(self):
        self.vals = []
        self.mvals = []

    def __len__(self):
        return len(self.vals)

    def push(self, val: int) -> None:
        if len(self) == 0:
            self.mvals.append(val)
        else:
            if self.mvals[-1] > val:
                self.mvals.append(val)
            else:
                self.mvals.append(self.mvals[-1])
        self.vals.append(val)

    def pop(self) -> None:
        self.mvals.pop()
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1] if len(self) > 0 else None

    def getMin(self) -> int:
        return self.mvals[-1] if len(self) > 0 else None


def main():
    stack = MinStack()
    stack.push(-304)
    stack.push(-22)
    stack.push(-404)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())


if __name__ == "__main__":
    main()
