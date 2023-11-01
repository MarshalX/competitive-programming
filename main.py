class Solution:
    squares = {i: i ** 2 for i in range(0, 10)}

    def squaresSumOfDigits(self, current: int) -> int:
        new = 0

        while current != 0:
            new += self.squares[current % 10]
            current //= 10

        return new

    def isHappy(self, n: int) -> bool:
        slow = self.squaresSumOfDigits(n)
        if slow == 1:
            return True

        fast = self.squaresSumOfDigits(self.squaresSumOfDigits(n))

        while slow != fast:
            slow = self.squaresSumOfDigits(slow)
            fast = self.squaresSumOfDigits(self.squaresSumOfDigits(fast))

            if slow == 1:
                return True

        return False


if __name__ == '__main__':
    cases = [
        0, 1, 19, 2
    ]

    for case in cases:
        print(Solution().isHappy(case))
