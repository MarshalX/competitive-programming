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
  int countCharacters(vector<string>& words, string chars) {
    map<char, int> m;
    for (const char c: chars) {
      m[c]++;
    }

    int res = 0;
    for (const string& word : words) {
      map<char, int> mCopy = m;
      for (char c : word) {
        mCopy[c]--;
      }

      bool toAdd = true;
      for (auto kv : mCopy) {
        if (kv.second < 0) {
          toAdd = false;
          break;
        }
      }

      if (toAdd) {
        res += word.length();
      }
    }

    return res;
  }
};


int main() {
  auto v = vector<string>{"hello","world","leetcode"}; // 10
  cout << Solution().countCharacters(v, "welldonehoneyr") << endl;

  return 0;
}
