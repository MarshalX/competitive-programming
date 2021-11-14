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

    auto p = vector<int>(needle.length());

    int i = 1;
    int j = 0;

    p[0] = 0;
    while (i < needle.length()) {
      if (needle[i] == needle[j]) {
        p[i] = j + 1;
        i++; j++;
      } else {
        if (j == 0) {
          p[i] = 0;
          i++;
        } else {
          j = p[j - 1];
        }
      }
    }

    i = 0;
    j = 0;
    while (i < haystack.length()) {
      if (haystack[i] == needle[j]) {
        i++; j++;
        if (j == needle.length()) {
          return i - j;
        }
      } else {
        if (j > 0) {
          j = p[j - 1];
        } else {
          i++;
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
