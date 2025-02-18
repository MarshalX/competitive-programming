class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]

        return res


if __name__ == '__main__':
    assert 'apbqcrqqqq' == Solution().mergeAlternately(word1 = 'abc', word2 = 'pqrqqqq')
    assert 'apbqcr' == Solution().mergeAlternately(word1 = 'abc', word2 = 'pqr')
    assert 'apbqrs' == Solution().mergeAlternately(word1 = 'ab', word2 = 'pqrs')
    assert 'apbqcd' == Solution().mergeAlternately(word1 = 'abcd', word2 = 'pq')
    assert 'ab' == Solution().mergeAlternately(word1 = 'a', word2 = 'b')
    assert 'ba' == Solution().mergeAlternately(word1 = 'b', word2 = 'a')
