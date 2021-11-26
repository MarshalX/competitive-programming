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
  string addStrings(string num1, string num2) {
    auto num = num2;
    auto numM = num1;
    if (num1.length() > num2.length()) {
      num = num1;
      numM = num2;
    }
    auto numMin = min(num1.length(), num2.length());

    int longPos = num.length();
    int tmp = 0;
    string res;
    for (int i = numMin - 1; i >= 0; --i) {
      longPos--;

      int o1 = numM[i] - '0';
      int o2 = num[longPos] - '0';

      int sum = o1 + o2 + tmp;
      tmp = sum / 10;

      char t = sum - (tmp * 10) + '0';
      res = t + res;

      cout << o1 << " " << o2 << " sum=" << sum << " rem=" << tmp << " add=" << t << endl;
    }

    for (int i = num.length() - numMin - 1; i >= 0; --i) {
      int o1 = num[i] - '0';
      int sum = o1 + tmp;
      tmp = sum / 10;

      char t = sum - (tmp * 10) + '0';
      res = t + res;
    }

    if (tmp != 0) {
      char t = tmp + '0';
      res = t + res;
    }

    return res;
  }
};


int main() {
  cout << Solution().addStrings("11", "123") << endl; // 134
  cout << Solution().addStrings("13", "129") << endl; // 142
  cout << Solution().addStrings("131", "129") << endl; // 260
  cout << Solution().addStrings("1", "2") << endl; // 3
  cout << Solution().addStrings("1", "22") << endl; // 23
  cout << Solution().addStrings("11", "2") << endl; // 13
  cout << Solution().addStrings("11", "22") << endl; // 33
  cout << Solution().addStrings("1", "9") << endl; // 10

  return 0;
}
