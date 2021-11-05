#include <iostream>

using namespace std;

class Solution {
public:
  bool isPalindrome(int x) {
    string s = to_string(x);
    int r = s.length() - 1;
    for (int l = 0; l < s.length(); ++l) {
      if (l == r) {
        break;
      }

      if (s[l] != s[r]) {
        return false;
      }

      r--;
    }

    return true;
  }
};

int main() {
  int x;
  while (1) {
    cin >> x;
    cout << ((new Solution())->isPalindrome(x) ? "true" : "false") << endl;
  }
  return 0;
}
