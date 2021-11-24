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
  int findShortestSubArray(vector<int>& nums) {
    auto m = map<int, int>();
    int res = 50000;

    for (int n:nums) {
      if (m.find(n) == m.end()) {
        m[n] = 1;
      } else {
        m[n] += 1;
      }
    }

    std::set<std::pair<int, int>> s;
    for (auto const &i : m) {
      s.emplace(i.second, i.first);
    }

    int max = -1;
    for (auto i = s.rbegin(); i != s.rend(); ++i) {
      if (max == -1) {
        max = i->first;
      }

      if (i->first < max) {
        break;
      }

      int start = -1;
      int stop = -1;
      for (int j = 0; j < nums.size(); ++j) {
        if (start == -1 && nums[j] == i->second) {
          start = j;
        }
        if (nums[j] == i->second) {
          stop = j;
        }
      }

      res = min(res, stop - start + 1);
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{1, 2, 2, 3, 1}; // 2
  auto v1 = vector<int>{1, 2, 2, 3, 1, 4, 2}; // 6
  auto v2 = vector<int>{1}; // 1
  cout << Solution().findShortestSubArray(v) << endl;
  cout << Solution().findShortestSubArray(v1) << endl;
  cout << Solution().findShortestSubArray(v2) << endl;

  return 0;
}
