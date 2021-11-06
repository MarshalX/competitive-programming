#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>

using namespace std;


class Solution {
public:
  string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 1) {
      return strs[0];
    }

    int minLen = 201;
    for (auto &i: strs) {
      minLen = min(minLen, (int)i.length());
    }

    string res = "";
    bool isEnd = false;
    for (int i = 0; i < minLen; ++i) {
      char cur = strs[0][i];
      for (int j = 1; j < strs.size(); ++j) {
        if (cur != strs[j][i]) { isEnd = true; break; }
        if (j == strs.size() - 1) { res += cur; }
      }

      if (isEnd) {
        break;
      }
    }

    return res;
  }
};

int main() {
  auto v = vector<string>{"flower","flow","flight"};
  auto v1 = vector<string>{"dog","racecar","car"};
  auto v3 = vector<string>{"cir","car"};
  cout << Solution().longestCommonPrefix(v) << endl;
  cout << Solution().longestCommonPrefix(v1) << endl;
  cout << Solution().longestCommonPrefix(v3) << endl;

  return 0;
}
