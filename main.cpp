#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>
#include <queue>

using namespace std;


class Solution {
public:
  int pivotIndex(vector<int>& nums) {
    vector<int> p;

    p.push_back(nums[0]);
    for (int i = 1; i < nums.size(); ++i) {
      p.push_back(p[i - 1] + nums[i]);
    }

    int last = nums.size() - 1;
    for (int i = 0; i < nums.size(); ++i) {
      if (i == 0) {
        if (p[last] - nums[i] == 0) {
          return 0;
        }
      } else if (p[i - 1] == p[last] - p[i]) {
        return i;
      }
    }

    return -1;
  }
};


int main() {
  auto v = vector<int>{1, 7, 3, 6, 5, 6};
  auto v1 = vector<int>{2, 1, -1};
  auto v3 = vector<int>{2, 1, -1};
  cout << Solution().pivotIndex(v) << endl;
  cout << Solution().pivotIndex(v1) << endl;
  cout << Solution().pivotIndex(v3) << endl;

  return 0;
}
