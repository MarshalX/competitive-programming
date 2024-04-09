class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count, res = 0, ''
        for c in s:
            init = count == 0
            count += 1 if c == '(' else -1

            if init or count == 0:
                continue

            res += c

        return res


if __name__ == '__main__':
    a = Solution().removeOuterParentheses('(()())(())')
    assert '()()()' == a
    a = Solution().removeOuterParentheses('(()())(())(()(()))')
    assert '()()()()(())' == a
    a = Solution().removeOuterParentheses('()()')
    assert '' == a
