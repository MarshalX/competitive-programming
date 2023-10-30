class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            i = (left + right) // 2
            s = i * i

            if s == x:
                return i

            if s > x:
                right = i - 1
            else:
                left = i + 1

        return right


if __name__ == '__main__':
    cases = [
        0, 1, 4, 8, 6
    ]

    for case in cases:
        print(Solution().mySqrt(case))
