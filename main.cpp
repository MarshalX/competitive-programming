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
    auto start = map<int, int>();
    auto stop = map<int, int>();
    int res = 50000;

    for (int j = 0; j < nums.size(); ++j) {
      if (m.find(nums[j]) == m.end()) {
        m[nums[j]] = 1;
      } else {
        m[nums[j]] += 1;
      }

      if (start.find(nums[j]) == start.end()) {
        start[nums[j]] = j;
      }
      stop[nums[j]] = j;
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

      res = min(res, stop[i->second] - start[i->second] + 1);
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
