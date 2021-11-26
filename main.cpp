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
    bool toAdd;
    for (const string& word : words) {
      for (char c : word) {
        m[c]--;
      }

      toAdd = true;
      for (auto kv : m) {
        if (kv.second < 0) {
          toAdd = false;
          break;
        }
      }

      if (toAdd) {
        res += word.length();
      }

      for (char c : word) {
        m[c]++;
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
