from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        last = len(s) - 1
        for cur in range(len(s) // 2):
            s[last], s[cur] = s[cur], s[last]
            last -= 1
