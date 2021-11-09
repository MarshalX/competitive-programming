#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>

using namespace std;


class Solution {
public:
  int getNonZeroPos(vector<int>& nums, int cur) {
    for (int i = cur; i < nums.size(); ++i) {
      if (nums[i] != 0) {
        return i;
      }
    }

    return -1;
  }

  void moveZeroes(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; ++i) {
      if (nums[i] == 0) {
        int nonZero = getNonZeroPos(nums, i + 1);
        if (nonZero != -1) {
          nums[i] = nums[nonZero];
          nums[nonZero] = 0;
        }
      }
    }
  }
};

int main() {
  vector<int> v = {0, 1, 0, 3, 12};
  Solution().moveZeroes(v);
  for (auto &i: v) {
    cout << i << " ";
  }

  return 0;
}
