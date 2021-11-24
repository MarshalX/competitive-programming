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
  int maxProfit(vector<int>& prices) {
    int l = 0;
    int r = 1;

    int res = 0;
    while (l < prices.size() && r < prices.size()) {
      if (prices[l] > prices[r]) {
        l = r;
      } else {
        res = max(res, prices[r] - prices[l]);
        r++;
      }
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{7, 1, 5, 3, 6, 4}; // 5
  auto v1 = vector<int>{7, 6, 4, 3, 1}; // 0
  auto v2 = vector<int>{1}; // 0
  auto v3 = vector<int>{2, 1, 4}; // 3
  cout << Solution().maxProfit(v) << endl;
  cout << Solution().maxProfit(v1) << endl;
  cout << Solution().maxProfit(v2) << endl;
  cout << Solution().maxProfit(v3) << endl;

  return 0;
}
