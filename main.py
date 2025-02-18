class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rules = {
            'I': {'V': 4, 'X': 9},
            'X': {'L': 40, 'C': 90},
            'C': {'D': 400, 'M': 900},
        }

        i = res = 0
        while i != len(s):
            if i < len(s) - 1 and s[i] in rules and s[i + 1] in rules[s[i]]:
                res += rules[s[i]][s[i + 1]]
                i += 1
            else:
                res += digits[s[i]]
            i += 1

        return res


if __name__ == '__main__':
    assert 3 == Solution().romanToInt('III')
    assert 58 == Solution().romanToInt('LVIII')
    assert 1994 == Solution().romanToInt('MCMXCIV')
