from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    cases = [
        [0],
        [9, 9, 9],
        [9, 8, 9],
        [1, 2, 9],
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
    ]

    for case in cases:
        print(Solution().plusOne(case))
