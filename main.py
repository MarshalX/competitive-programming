from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(lambda: 0)
        for num in nums:
            d[num] += 1
            if d[num] > 1:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 1]))
    print(Solution().containsDuplicate([1, 2, 3, 4]))
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
