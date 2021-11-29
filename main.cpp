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
  vector<int> sumZero(int n) {
    vector<int> res;

    int half = n / 2;
    int tmp = 0;

    int i = 1;
    for (int j = 0; j < half; ++j) {
      if (j == half - 1) {
        int t = abs(tmp - n);
        if (t < i) t = i;
        res.push_back(t);
        res.push_back(-t);
      } else {
        res.push_back(i);
        res.push_back(-i);
        tmp += i;
        i++;
      }
    }

    if (n % 2 != 0) {
      res.push_back(0);
    }

    return res;
  }
};


int main() {
  auto res = Solution().sumZero(5);
//  auto res = Solution().sumZero(2);
//  auto res = Solution().sumZero(8);

  for (const int i : res) {
    cout << i << " ";
  }

  return 0;
}
