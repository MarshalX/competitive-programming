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
  map<char, char> m = {
      {'(', ')'},
      {'[', ']'},
      {'{', '}'},
  };

  bool isValid(string s) {
    stack<char> st = stack<char>();
    for (int i = 0; i < s.length(); ++i) {
      if (m.find(s[i]) != m.end()) {
        st.push(s[i]);
      } else {
        if (st.empty()) {
          return false;
        }

        if (m[st.top()] != s[i]) {
          return false;
        }
        st.pop();
      }
    }

    return st.empty();
  }
};

int main() {
  cout << Solution().isValid("()") << endl;
  cout << Solution().isValid("]") << endl;

  return 0;
}
