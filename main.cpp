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
    int res = -10e5;
    int tmpSum = 0;

    for (int num : nums) {
      tmpSum += num;
      tmpSum = max(tmpSum, num);
      res = max(res, tmpSum);
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{-2, 1, -3, 4, -1, 2, 1, -5, 4};
  auto v1 = vector<int>{5, 4, -1, 7, 8};
  auto v3 = vector<int>{-2, 1};
  auto v4 = vector<int>{-1};
  cout << Solution().maxSubArray(v) << endl;
  cout << Solution().maxSubArray(v1) << endl;
  cout << Solution().maxSubArray(v3) << endl;
  cout << Solution().maxSubArray(v4) << endl;

  return 0;
}
