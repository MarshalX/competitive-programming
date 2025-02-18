from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        interested_word = 'balloon'
        interesting_letters = set(list(interested_word))

        d = defaultdict(int)
        for letter in text:
            if letter in interesting_letters:
                d[letter] += 1

        if len(d) != len(interesting_letters):
            return 0

        d['l'] = int(d['l'] / 2)
        d['o'] = int(d['o'] / 2)
        return min(d.values())
