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

    int startIndex;
    for (int i = 0; i < haystack.length(); ++i) {
      startIndex = i;
      for (int j = 0; j < needle.length(); ++j) {
         if (i + j > haystack.length() - 1) { break; }

        if (haystack[i + j] != needle[j]) {
          break;
        } else if (j == needle.length() - 1) {
          return startIndex;
        }
      }
    }

    return -1;
  }
};


int main() {
  cout << Solution().strStr("ooo", "ooooooooo") << endl;
  cout << Solution().strStr("hello", "ll") << endl;

  return 0;
}
