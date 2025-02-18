from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, range_part, range_started = [], None, False
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                if not range_started:
                    range_part = f'{nums[i]}->'
                    range_started = True
            elif range_started:
                res.append(f'{range_part}{nums[i]}')
                range_started = False
            else:
                res.append(f'{nums[i]}')

        return res

if __name__ == '__main__':
    assert [] == Solution().summaryRanges([])
    assert ['1', '3'] == Solution().summaryRanges([1, 3])
    assert ['1->3'] == Solution().summaryRanges([1, 2, 3])
    assert ['0->2','4->5','7'] == Solution().summaryRanges([0,1,2,4,5,7])
    assert ['0','2->4','6','8->9']== Solution().summaryRanges([0,2,3,4,6,8,9])
