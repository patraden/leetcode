from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [0] * n

        # give candies from left to right
        for i in range(n):
            candies[i] = 1
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # give candies from right to left
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1] and candies[i + 1] + 1 > candies[i]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


def main():
    print(Solution().candy([1, 2, 5, 4, 3, 2, 1]))
    # print(Solution().candy([1, 2, 2]))


if __name__ == "__main__":
    main()
