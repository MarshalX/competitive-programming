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
  vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    map<int, int> powers;

    int tPower;
    for (int i = 0; i < mat.size(); ++i) {
      tPower = 0;
      for (int j = 0; j < mat[i].size(); ++j) {
        if (mat[i][j] == 1) {
          tPower++;
        } else {
          powers[i] = tPower;
          break;
        }

        if (j == mat[i].size() - 1) {
          powers[i] = tPower;
        }
      }
    }

    set<pair<int, int>> s;
    for (const auto kv: powers) {
      s.emplace(kv.second, kv.first);
    }

    vector<int> res;
    for (const auto & i : s) {
      if (k == 0) break;
      k--;
      res.push_back(i.second);
    }

    return res;
  }
};


int main() {
  auto v = vector<vector<int>>{{1, 1, 0, 0, 0},
                               {1, 1, 1, 1, 0},
                               {1, 0, 0, 0, 0},
                               {1, 1, 0, 0, 0},
                               {1, 1, 1, 1, 1}}; // [2, 0, 3]
  auto v1 = vector<vector<int>>{{1, 0},
                                {1, 0},
                                {1, 0},
                                {1, 1}};
  auto r = Solution().kWeakestRows(v, 3);
//  auto r = Solution().kWeakestRows(v1, 4);
  for (int n:r) {
    cout << n << " ";
  }

  return 0;
}
