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
  int findMiddleIndex(vector<int>& nums) {
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
  auto v = vector<int>{2, 3, -1, 8, 4};
  auto v1 = vector<int>{1, -1, 4};
  cout << Solution().findMiddleIndex(v) << endl;
  cout << Solution().findMiddleIndex(v1) << endl;

  return 0;
}
