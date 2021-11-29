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
  void solver(vector<vector<int>>& res, vector<int>& nums, int k) {
    if (k == nums.size() - 1) {
      res.emplace_back();
      res.push_back({nums[k]});
      return;
    }

    solver(res, nums, k + 1);
    int size = res.size();
    for (int i = 0; i < size; ++i) {
      auto t = res[i];
      t.push_back(nums[k]);
      res.push_back(t);
    }
  }

  vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;
    solver(res, nums, 0);
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
