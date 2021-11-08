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
  int removeElement(vector<int>& nums, int val) {
    int k = 0;

    if (nums.empty()) {
      return k;
    }

    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] != val) {
        nums[k] = nums[i];
        k++;
      }
    }

    return k;
  }
};

int main() {
  vector<int> v = {0, 1, 2, 2, 3, 0, 4, 2};
  cout << Solution().removeElement(v, 2) << endl;

  return 0;
}
