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
  int strStr(string haystack, string needle) {
    if (needle.empty()) {
      return 0;
    }

    auto t = vector<int>(needle.length());

    int pos = 1;
    int cnd = 0;

    t[0] = -1;
    while (pos < needle.length()) {
      if (needle[pos] == needle[cnd]) {
        t[pos] = t[cnd];
      } else {
        t[pos] = cnd;
        while (cnd >= 0 && needle[pos] != needle[cnd]) {
          cnd = t[cnd];
        }
      }

      pos++;
      cnd++;
    }

    int j = 0;
    int k = 0;
    while (j < haystack.length()) {
      if (needle[k] == haystack[j]) {
        j++;
        k++;
        if (k == needle.length()) {
          return j - k;
        }
      } else {
        k = t[k];
        if (k < 0) {
          j++;
          k++;
        }
      }
    }

    return -1;
  }
};


int main() {
  cout << Solution().strStr("aaaaa", "bba") << endl;
  cout << Solution().strStr("", "a") << endl;
  cout << Solution().strStr("a", "a") << endl;
  cout << Solution().strStr("ooo", "ooooooooo") << endl;
  cout << Solution().strStr("hello", "ll") << endl;

  return 0;
}
