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
  vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;

    int size = nums.size();
    for (int i = 0; i < (1 << size); ++i) {
      vector<int> subset;
      for (int j = 0; j < size; ++j) {
        if (i & (1 << j)) {
          subset.push_back(nums[j]);
        }
      }

      res.push_back(subset);
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{1, 2, 3};
  auto v1 = vector<int>{0};
  auto res = Solution().subsets(v);
//  auto res = Solution().subsets(v1);

  for (const auto& r : res) {
    for (const auto i : r) {
      cout << i << " ";
    }
    cout << endl;
  }

  return 0;
}
