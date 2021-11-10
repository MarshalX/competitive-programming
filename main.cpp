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
    for (int i = 0; i < height.size(); ++i) {
      for (int j = i + 1; j < height.size(); ++j) {
        res = max(res, min(height[i], height[j]) * (j - i));
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
