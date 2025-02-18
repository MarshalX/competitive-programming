from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1

        for letter in t:
            if letter not in d:
                return False

            if d[letter] > 0:
                d[letter] -= 1
            else:
                return False

        for letters_count in d.values():
            if letters_count != 0:
                return False

        return True
