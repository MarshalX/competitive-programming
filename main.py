class Solution:
    def myAtoi(self, s: str) -> int:
        sign, sign_buf, buf = 1, '', ''
        for c in s:
            if not buf and not sign_buf and c == ' ':
                continue

            if not buf and not sign_buf and c in {'-', '+'}:
                sign, sign_buf = -1 if c == '-' else 1, c
                continue

            if not c.isdigit():
                break

            buf += c

        num = sign * int(buf or 0)
        num = min(2 ** 31 - 1, num)
        return max(-2 ** 31, num)


if __name__ == '__main__':
    a = Solution().myAtoi('')
    assert 0 == a
    a = Solution().myAtoi('42')
    assert 42 == a
    a = Solution().myAtoi('+-12')
    assert 0 == a
    a = Solution().myAtoi('  +  413')
    assert 0 == a
    a = Solution().myAtoi('42-')
    assert 42 == a
    a = Solution().myAtoi('   -42')
    assert -42 == a
    a = Solution().myAtoi('   -4  2')
    assert -4 == a
    a = Solution().myAtoi('4193 with words')
    assert 4193 == a
    a = Solution().myAtoi('41.93')
    assert 41 == a
    a = Solution().myAtoi('2147483648')
    assert 2_147_483_647 == a
    a = Solution().myAtoi('-2147483649')
    assert -2_147_483_648 == a
