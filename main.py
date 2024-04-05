from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a, b, c, d = (list(digits) + ['0'] * 4)[:4]
        m = {
            '0': [''],
            '1 ': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        for l1 in m[a]:
            for l2 in m[b]:
                for l3 in m[c]:
                    for l4 in m[d]:
                        if r := l1 + l2 + l3 + l4:
                            res.append(r)

        return res


if __name__ == '__main__':
    a = Solution().letterCombinations('23')
    assert ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] == a
