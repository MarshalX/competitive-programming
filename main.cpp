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
    for (int i = 0; i < 32; ++i) {
      if (i == 31 && n < 0) {
        if (n == (1L << i) - 1) return true;
      } else if (n == (1 << i)) return true;
    }

    return false;
  }
};


int main() {
  cout << Solution().isPowerOfTwo(1) << endl;
  cout << Solution().isPowerOfTwo(16) << endl;
  cout << Solution().isPowerOfTwo(-16) << endl;
  cout << Solution().isPowerOfTwo(3) << endl;
  cout << Solution().isPowerOfTwo(-2147483648) << endl; // 0
  cout << Solution().isPowerOfTwo(2147483647) << endl; // 0

  return 0;
}
