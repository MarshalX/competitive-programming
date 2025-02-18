from collections import defaultdict


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        interesting_letters = set(list(target))

        d = defaultdict(int)
        for letter in s:
            if letter in interesting_letters:
                d[letter] += 1

        res = 0
        while True:
            for letter in target:
                if letter not in d:
                    return res

                if d[letter] == 0:
                    return res

                d[letter] -= 1

            res += 1
