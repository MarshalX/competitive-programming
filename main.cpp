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
  void moveZeroes(vector<int>& nums) {
    int zeroCount = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == 0) {
        zeroCount += 1;
      } else  {
        nums[i - zeroCount] = nums[i];
      }
    }

    for (int i = nums.size() - 1; i > nums.size() - 1 - zeroCount; --i) {
      nums[i] = 0;
    }
  }
};

int main() {
  vector<int> v = {0};
//  vector<int> v = {0, 1, 0, 3, 12};
  Solution().moveZeroes(v);
  for (auto &i: v) {
    cout << i << " ";
  }

  return 0;
}
