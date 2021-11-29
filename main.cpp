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
    int num = x ^ y;
    while (num) {
      res += num % 2;
      num = num >> 1;
    }
    return res;
  }
};


int main() {
  cout << Solution().hammingDistance(1, 4) << endl;
  cout << Solution().hammingDistance(3, 1) << endl;

  return 0;
}
