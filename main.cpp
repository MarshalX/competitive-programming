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
  vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    priority_queue<pair<int, int>,vector<pair<int, int>>,greater<pair<int, int>>> powers;

    for (int i = 0; i < mat.size(); ++i) {
      powers.push({count(mat[i].begin(), mat[i].end(), 1), i});
    }

    vector<int> res;
    while (!powers.empty()) {
      if (k == 0) break;
      k--;
      res.push_back(powers.top().second);
      powers.pop();
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
