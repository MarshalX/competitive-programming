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
  int findComplement(int num) {
    int leadingZerosCount = num ? __builtin_clz(num) : 31;
    int bitsCount = 32 - leadingZerosCount;
    for (int i = 0; i < bitsCount; ++i) num = num ^ (1 << i);
    return num;
  }
};


int main() {
  cout << Solution().findComplement(5) << endl;
  cout << Solution().findComplement(1) << endl;

  return 0;
}
