class Solution:
    def maxDepth(self, s: str) -> int:
        result = current = 0
        for c in s:
            if c == '(':
                current += 1
                result = max(result, current)
            elif c == ')':
                current -= 1

        return result


if __name__ == '__main__':
    a = Solution().maxDepth('(1+(2*3)+((8)/4))+1')
    assert 3 == a
    a = Solution().maxDepth('')
    assert 0 == a
    a = Solution().maxDepth('(1)+((2))+(((3)))"')
    assert 3 == a
