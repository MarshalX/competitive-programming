#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>

using namespace std;


class Solution {
public:
  int minStartValue(vector<int>& nums) {
    int res = 1;
    int sum = 0;
    for (int num : nums) {
      sum += num;
      if (sum < 1) {
        int tmp = sum * - 1 + 1;
        if (tmp > res) {
          res = tmp;
        }
      }
    }
    return res;
  }
};

int main() {
  vector<int> v = {-3, 2, -3, 4, 2};
  vector<int> v2 = {1, -2, -3};
  vector<int> v3 = {1, 2};
  cout << Solution().minStartValue(v) << endl;
  cout << Solution().minStartValue(v2) << endl;
  cout << Solution().minStartValue(v3) << endl;

  return 0;
}
