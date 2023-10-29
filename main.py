class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        n = len(s) - 1
        while n >= 0:
            if s[n].isspace() and res != 0:
                return res
            if not s[n].isspace():
                res += 1

            n -= 1

        return res


if __name__ == '__main__':
    cases = [
        "a",
        "Hello World",
        "   fly me   to   the moon  ",
    ]

    for case in cases:
        print(Solution().lengthOfLastWord(case))
