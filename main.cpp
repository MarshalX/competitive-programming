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
  int removeDuplicates(vector<int>& nums) {
    int k = 0;

    if (nums.empty()) {
      return k;
    }

    for (int i = 0; i < nums.size() - 1; ++i) {
      if (nums[i] != nums[i + 1]) {
        k++;
        nums[k] = nums[i + 1];
      }
    }

    return k + 1;
  }
};

int main() {
  vector<int> v = {1, 1, 1, 1, 1, 1};
//  vector<int> v = {1, 1, 2};
//  vector<int> v = {1, 2};
//  vector<int> v = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
  cout << Solution().removeDuplicates(v) << endl;

  return 0;
}
