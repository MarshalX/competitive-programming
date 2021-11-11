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
  int maxArea(vector<int>& height) {
    int res = 0;

    int l = 0;
    int r = height.size() - 1;

    while (l < r) {
      int hl = height[l];
      int hr = height[r];

      res = max(res, min(height[l], height[r]) * (r - l));

      if (hl < hr) {
        l++;
      } else {
        r--;
      }
    }

    return res;
  }
};


int main() {
//  vector<int> v = {1, 8, 6, 2, 5, 4, 8, 3, 7};
//  vector<int> v = {1, 1};
//  vector<int> v = {4, 3, 2, 1, 4};
//  vector<int> v = {1, 2, 1};
//  vector<int> v = {2, 3, 4, 5, 18, 17, 6};
//  vector<int> v = {2, 1};
  vector<int> v = {1, 3, 2, 5, 25, 24, 5};
  vector<int> v2 = {1, 2, 3, 4, 5, 25, 24, 3, 4};
  cout << Solution().maxArea(v) << endl;
  cout << Solution().maxArea(v2) << endl;

  return 0;
}
