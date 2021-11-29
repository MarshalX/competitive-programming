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
  int hammingWeight(uint32_t n) {
    int res = 0;
    for (int i = 0; i < 32; ++i) {
      if ((n & (1 << i))) {
        res++;
      }
    }
    return res;
  }
};


int main() {
  // rly idk how to run it locally ;d
  return 0;
}
