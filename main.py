class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = 0

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid + 1):
                res = mid + 1

            if not isBadVersion(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == '__main__':
    cases = [
        5, 6, 10
    ]

    for case in cases:
        print(Solution().firstBadVersion(case))
