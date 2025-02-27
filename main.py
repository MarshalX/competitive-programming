from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j

            stack.append(i)

        return res


if __name__ == '__main__':
    assert [0] == Solution().dailyTemperatures([73])
    assert [1, 0] == Solution().dailyTemperatures([73, 74])
    assert [1,1,4,2,1,1,0,0] == Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
    assert [1,1,1,0] == Solution().dailyTemperatures([30,40,50,60])
