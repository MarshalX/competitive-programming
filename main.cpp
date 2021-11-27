#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>
#include <queue>

using namespace std;


class NumArray {
public:
  vector<int> p;

  NumArray(vector<int>& nums) {
    p.push_back(nums[0]);
    for (int i = 1; i < nums.size(); ++i) {
      p.push_back(p[i - 1] + nums[i]);
    }
  }

  int sumRange(int left, int right) {
    if (left > 0) {
      return p[right] - p[left - 1];
    } else {
      return p[right];
    }
  }
};


int main() {
  auto v = vector<int>{-2, 0, 3, -5, 2, -1};
  auto n = NumArray(v);
  cout << n.sumRange(0, 2) << endl;
  cout << n.sumRange(2, 5) << endl;
  cout << n.sumRange(0, 5) << endl;

  return 0;
}
