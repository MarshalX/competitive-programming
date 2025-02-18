from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        interested_word = 'balloon'
        interesting_letters = set(list(interested_word))

        d = defaultdict(int)
        for letter in text:
            if letter in interesting_letters:
                d[letter] += 1

        res = 0
        while True:
            for letter in interested_word:
                if letter not in d:
                    return res

                if d[letter] == 0:
                    return res

                d[letter] -= 1

            res += 1
