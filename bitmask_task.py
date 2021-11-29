"""
Subset Sum

You are given N numbers. Check if there is a subset
of them, with the sum equal to target value S.

N <= 20

Own edit: return the found subset.
Own edit2: return all possible subsets.
"""


# O(2^n * n)
def solution(nums: list[int], s: int) -> list[int]:
    size = len(nums)
    subset_all = []
    for mask in range(1 << size):     # AKA 2 ** size
        subset = []
        subset_sum = 0
        for i in range(size):
            if mask & (1 << i):
                subset.append(nums[i])
                subset_sum += nums[i]

        if subset_sum == s:
            subset_all.append(subset)

    return subset_all


if __name__ == '__main__':
    print(solution([20], 20))
    print(solution([1, 15, 3, 4], 20))
    print(solution([1, 15, 3, 5], 20))
    print(solution([1, 15, 3, 6], 20))
    print(solution([1, 15, 3, 4, 5], 20))
    # офигеть вау меня это впечатлило
