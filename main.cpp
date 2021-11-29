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
  vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    map<vector<int>, bool> m;
    vector<vector<int>> res;

    int size = nums.size();
    for (int i = 0; i < (1 << size); ++i) {
      vector<int> subset;
      for (int j = 0; j < size; ++j) {
        if (i & (1 << j)) {
          subset.push_back(nums[j]);
        }
      }

      m[subset] = true;
    }

    for (const auto kv : m) {
      res.push_back(kv.first);
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{1, 2, 2};
  auto v1 = vector<int>{0};
  auto v3 = vector<int>{4, 4, 4, 1, 4};
//  auto res = Solution().subsetsWithDup(v);
//  auto res = Solution().subsetsWithDup(v1);
  auto res = Solution().subsetsWithDup(v3);

  for (const auto& r : res) {
    for (const auto i : r) {
      cout << i << " ";
    }
    cout << endl;
  }

  return 0;
}
