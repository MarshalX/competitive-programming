class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for l in s:
            top = stack[-1] if stack else None
            if l == 'B' and top == 'A':
                stack.pop()
            elif l == 'D' and top == 'C':
                stack.pop()
            else:
                stack.append(l)

        return len(stack)


if __name__ == '__main__':
    a = Solution().minLength('ABFCACDB')
    assert a == 2
    a = Solution().minLength('ACBBD')
    assert a == 5
    a = Solution().minLength('ACDCDCDCDB')
    assert a == 0
    a = Solution().minLength('ACDCDFCDCDB')
    assert a == 3
