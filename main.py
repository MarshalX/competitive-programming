class Solution:
    def isHappy(self, n: int) -> bool:
        squares = {i: i ** 2 for i in range(0, 10)}
        known = set()

        while True:
            new = 0
            while n != 0:
                new += squares[(n % 10)]
                n //= 10

            if new == 1:
                return True
            if new in known:
                return False

            n = new
            known.add(new)


if __name__ == '__main__':
    cases = [
        0, 1, 19, 2
    ]

    for case in cases:
        print(Solution().isHappy(case))
