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
    int res = num;

    int i = 0;
    while (num != 0) {
      i++;
      num >>= 1;
    }

    for (int j = 0; j < i; ++j) {
      res = res ^ (1 << j);
    }

    return res;
  }
};


int main() {
  cout << Solution().findComplement(5) << endl;
  cout << Solution().findComplement(1) << endl;

  return 0;
}
