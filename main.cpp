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
  int maxSubArray(vector<int>& nums) {
    auto p = vector<int>(nums.size());
    p[0] = nums[0];

    int res = p[0];
    for (int i = 1; i < nums.size(); ++i) {
      p[i] = p[i - 1] + nums[i];
    }

    for (auto &n: p) {
      cout << n << " ";
    }
    cout << endl;

    for (int i = 0; i < p.size(); ++i) {
      for (int j = i + 1; j < p.size(); ++j) {
        int sum = p[j];
        res = max(res, sum);

        sum = p[j] - p[i];
        res = max(res, sum);

      }
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{-2, 1, -3, 4, -1, 2, 1, -5, 4};
  auto v1 = vector<int>{5, 4, -1, 7, 8};
  auto v3 = vector<int>{-2, 1};
  cout << Solution().maxSubArray(v) << endl;
  cout << Solution().maxSubArray(v1) << endl;
  cout << Solution().maxSubArray(v3) << endl;

  return 0;
}
