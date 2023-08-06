from heapq import *


class DinnerPlates:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]
        self.avail_idx = []

    def push(self, val):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        if not self.avail_idx:
            self.stacks[-1].append(val)
        else:
            idx = heappop(self.avail_idx)
            self.stacks[idx].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heappush(self.avail_idx, index)
            return self.stacks[index].pop()

        return -1


def main():
    plates = DinnerPlates(2)
    plates.push(1)
    plates.push(2)
    plates.push(3)
    plates.push(4)
    print(plates.stacks)
    print(plates.avail_idx)
    print("=" * 50)
    # plates.popAtStack(0)
    # plates.push(20)
    # plates.push(21)
    # plates.popAtStack(0)
    # plates.popAtStack(2)
    # print(plates.pop())
    # print(plates.pop())
    # print(plates.pop())
    # print(plates.pop())
    # print(plates.pop())
    # print(plates.stacks)
    # print(plates.left)
    # print("=" * 50)


if __name__ == "__main__":
    main()
