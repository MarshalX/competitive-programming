class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        s, p = [], 0
        for n in num:
            while s and s[-1] > n and k:
                s.pop()
                k -= 1
            s.append(n)

        if k != 0:
            s = s[:-k]

        res = ''
        start, non_zero = True, False
        for n in s:
            if n == '0' and start:
                continue

            start = False
            if n != '0':
                non_zero = True

            res += n

        if not non_zero:
            return '0'

        return res


if __name__ == '__main__':
    a = Solution().removeKdigits(num='1432219', k=3)
    assert '1219' == a
    a = Solution().removeKdigits(num='10200', k=1)
    assert '200' == a
    a = Solution().removeKdigits(num='10', k=2)
    assert '0' == a
    a = Solution().removeKdigits(num='10', k=1)
    assert '0' == a
    a = Solution().removeKdigits(num='9', k=1)
    assert '0' == a
    a = Solution().removeKdigits(num='112', k=1)
    assert '11' == a
    a = Solution().removeKdigits(num='111', k=1)
    assert '11' == a
    a = Solution().removeKdigits(num='12345', k=2)
    assert '123' == a
