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

    memset(&nums[nums.size()- zeroCount], 0, sizeof(int) * zeroCount);
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
