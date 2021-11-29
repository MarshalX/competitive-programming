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
  int largestAltitude(vector<int>& gain) {
    int res = 0;

    vector<int> p;
    p.push_back(0);
    for (int i = 1; i <= gain.size(); ++i) {
      p.push_back(p[i - 1] + gain[i - 1]);
      res = max(res, p.back());
    }

    return res;
  }
};


int main() {
  auto v = vector<int>{-5, 1, 5, 0, -7};
  auto v1 = vector<int>{-4, -3, -2, -1, 4, 3, 2};
  cout << Solution().largestAltitude(v) << endl;
  cout << Solution().largestAltitude(v1) << endl;

  return 0;
}
