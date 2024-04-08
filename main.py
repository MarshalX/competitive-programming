from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [i for i in nums if i & 1 == 1]
        even = [i for i in nums if i & 1 != 1]

        result = []
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])

        return result


if __name__ == '__main__':
    a = Solution().sortArrayByParityII([3, 4])
    assert [4, 3] == a
    a = Solution().sortArrayByParityII([4, 1, 2, 1])
    print(a)
    a = Solution().sortArrayByParityII([2, 3])
    assert [2, 3] == a
    a = Solution().sortArrayByParityII([2, 2, 2, 2, 1, 1, 1, 1])
    print(a)
    a = Solution().sortArrayByParityII([2, 2, 2, 2, 2, 1, 1, 1, 1, 1])
    print(a)
