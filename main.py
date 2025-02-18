from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]

        res = ''
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            res += first[i]

        return res


if __name__ == '__main__':
    assert 'fl' == Solution().longestCommonPrefix(['flower','flow','flight'])
    assert '' == Solution().longestCommonPrefix(['dog','racecar','car'])
