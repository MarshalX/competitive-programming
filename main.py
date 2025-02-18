class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        si = 0
        for i in t:
            if i == s[si]:
                si += 1

            if si == len(s):
                return True

        return False


if __name__ == '__main__':
    assert True == Solution().isSubsequence(s = 'abc', t = 'ahbgdc')
    assert False == Solution().isSubsequence(s = 'axc', t = 'ahbgdc')
