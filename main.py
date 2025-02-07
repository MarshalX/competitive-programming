class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        saved_space = 0
        for l in s:
            if not len(stack):
                stack.append(l)
                continue

            top = stack[len(stack) - 1]

            if l == 'B' and top == 'A':
                saved_space += 2
                stack.pop()
                continue
            elif l == 'D' and top == 'C':
                saved_space += 2
                stack.pop()
                continue
            else:
                stack.append(l)

        return len(s) - saved_space


if __name__ == '__main__':
    a = Solution().minLength('ABFCACDB')
    assert a == 2
    a = Solution().minLength('ACBBD')
    assert a == 5
    a = Solution().minLength('ACDCDCDCDB')
    assert a == 0
    a = Solution().minLength('ACDCDFCDCDB')
    assert a == 3
