class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        if self.current < len(self.history) - 1:
            self.history = self.history[:self.current + 1]
            self.current = len(self.history) - 1

        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current -= steps if steps <= self.current else self.current
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current += steps if (steps + self.current) < len(self.history) else len(self.history) - self.current - 1
        return self.history[self.current]


def main():
    h = BrowserHistory("leetcode.com")
    print(h.visit("google.com"))
    print(h.visit("facebook.com"))
    print(h.visit("youtube.com"))
    print(h.back(1))
    print(h.back(1))
    print(h.forward(1))
    print(h.visit("linkedin.com"))
    print(h.forward(2))
    print(h.back(2))
    print(h.back(7))
    print("hist: ", h.history)
    print("current:", h.current)


if __name__ == "__main__":
    main()
