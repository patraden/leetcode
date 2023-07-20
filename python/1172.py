import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = []  # contains pointers to non-full stacks at the current state
        self.right = []  # contains pointers to none-empty stacks at the current state
        self.stacks = []

    def push(self, val: int) -> None:
        if not self.left:
            self.stacks.append([])
            heapq.heappush(self.left, len(self.stacks) - 1)

        l = self.left[0]
        while l >= len(self.stacks):
            self.stacks.append([])
            l = self.left[0]

        if not self.right or (-self.right[0]) < l:
            heapq.heappush(self.right, -l)

        self.stacks[l].append(val)

        #  stack became full, thus left pointer should be removed
        if len(self.stacks[l]) == self.capacity:
            heapq.heappop(self.left)

    def pop(self) -> int:
        if not self.right:
            return -1

        r = - self.right[0]

        #  stack became not full, thus this pointer should be added to left pointers
        if len(self.stacks[r]) == self.capacity:
            heapq.heappush(self.left, r)

        val = self.stacks[r].pop()

        # clean potential empty stacks after pop and popAt methods
        while self.stacks and len(self.stacks[r]) == 0:
            assert (r + 1) == len(self.stacks)
            self.stacks.pop()
            heapq.heappop(self.right)
            if self.right:
                r = - self.right[0]
            else:
                assert len(self.stacks) == 0
                break

        return val

    def popAtStack(self, index: int) -> int:
        if not (0 <= index < len(self.stacks)) or len(self.stacks[index]) == 0:
            return -1

        #  stack became not full, thus this pointer should be added to left pointers
        if len(self.stacks[index]) == self.capacity:
            heapq.heappush(self.left, index)

        return self.stacks[index].pop()


def main():
    plates = DinnerPlates(2)
    plates.push(1)
    plates.push(2)
    plates.push(3)
    plates.push(4)
    plates.push(5)
    print(plates.stacks)
    print(plates.left)
    print(plates.right)
    print("=" * 50)
    plates.popAtStack(0)
    plates.push(20)
    plates.push(21)
    plates.popAtStack(0)
    plates.popAtStack(2)
    print(plates.pop())
    print(plates.pop())
    print(plates.pop())
    print(plates.pop())
    print(plates.pop())
    print(plates.stacks)
    print(plates.left)
    print(plates.right)
    print("=" * 50)


if __name__ == "__main__":
    main()
