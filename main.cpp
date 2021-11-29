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
  int hammingDistance(int x, int y) {
    int res = 0;
    for (int i = 0; i < 32; ++i) {
      bool e1 = x & (1 << i);
      bool e2 = y & (1 << i);
      if (e1 != e2) {
        res++;
      }
    }
    return res;
  }
};


int main() {
  cout << Solution().hammingDistance(1, 4) << endl;
  cout << Solution().hammingDistance(3, 1) << endl;

  return 0;
}
