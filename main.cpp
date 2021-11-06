#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>

using namespace std;


class Solution {
public:
  vector<string> stringMatching(vector<string>& words) {
    vector<string> res;
    set<string> u;
    for (int i = 0; i < words.size(); ++i) {
      for (int j = 0; j < words.size(); ++j) {
        if (i == j) { continue; }
        if (words[i].find(words[j]) != -1) {
          if (u.find(words[j]) == u.end()) {
            u.insert(words[j]);
            res.push_back(words[j]);
          }
        }
      }
    }
    return res;
  }
};

int main() {

  return 0;
}
