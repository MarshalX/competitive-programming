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
    map<int, int> m;
    map<int, vector<int>> pos;
    int res = INT_MAX;

    int maxDegree = 0;
    for (int & num : nums) {
      m[num] += 1;

      maxDegree = max(maxDegree, m[num]);
    }

    for (int i = 0; i < nums.size(); ++i) {
      if (m[nums[i]] == maxDegree && pos.find(nums[i]) == pos.end()) {
        pos[nums[i]].emplace_back(i);
        pos[nums[i]].push_back(-1);
      }
    }

    for (int i = nums.size() - 1; i >= 0; --i) {
      if (m[nums[i]] == maxDegree && pos[nums[i]][1] == -1) {
        pos[nums[i]][1] = i;
      }
    }

    set<pair<int, int>> s;
    for (auto const &i : m) {
      s.emplace(i.second, i.first);
    }

    for (auto i = s.rbegin(); i != s.rend(); ++i) {
      if (i->first < maxDegree) {
        break;
      }

      res = min(res, pos[i->second][1] - pos[i->second][0] + 1);
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
