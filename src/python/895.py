class FreqStack:

    def __init__(self):
        self.frequencies = {}
        self.hash = {}
        self.max_frequency = 0

    def push(self, val: int) -> None:
        if self.hash.get(val, 0) == self.max_frequency:
            self.frequencies[self.max_frequency + 1] = [val]
            self.max_frequency += 1
            self.hash[val] = self.hash.get(val, 0) + 1
        else:
            self.hash[val] = self.hash.get(val, 0) + 1
            self.frequencies[self.hash[val]].append(val)

    def pop(self) -> int:
        if self.max_frequency > 0:
            val = self.frequencies.get(self.max_frequency).pop()
            self.hash[val] -= 1
            if self.hash[val] == 0:
                self.hash.pop(val)

            if not self.frequencies.get(self.max_frequency):
                self.frequencies.pop(self.max_frequency)
                self.max_frequency -= 1
            return val


def main():
    s = FreqStack()
    s.push(5)
    s.push(7)
    s.push(5)
    s.push(7)
    s.push(4)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == "__main__":
    main()
