#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>

using namespace std;


class Solution {
public:
  int calculate(string s) {
    string operand = "";
    for (int i = 0; i < s.size(); ++i) {
      if (s[i] == ' ') { continue; }
      if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
        cout << operand << " " << s[i] << " ";
        operand = "";
      } else {
        operand += s[i];
      }
    }

    if (!operand.empty()) {
      cout << operand << endl;
    }

    // TODO polish notation

    return 0;
  }
};

int main() {
  cout << Solution().calculate("3 + 5 / 2 ") << endl;
  cout << (int)'0'<< " " << (int)'9'<< endl;
  return 0;
}
