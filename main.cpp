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
  bool isPowerOfTwo(int n) {
    if (n == -(1L << 31)) return false;
    return __builtin_popcount(n) == 1;
  }
};


int main() {
  return 0;
}
