#include <iostream>
#include <vector>
#include <map>

using namespace std;


class Solution {
public:
  map<char, int> m = map<char, int>{
      {'I', 1},
      {'V', 5},
      {'X', 10},
      {'L', 50},
      {'C', 100},
      {'D', 500},
      {'M', 1000},
  };

  int romanToInt(string s) {
    int number = 0;
    for (int i = 0; i < s.length(); ++i) {
      char next = i == s.length() - 1 ? '-' : s[i + 1];

      if (
          (s[i] == 'I' && (next == 'V' || next == 'X')) |
          (s[i] == 'X' && (next == 'L' || next == 'C')) |
          (s[i] == 'C' && (next == 'D' || next == 'M'))
          ) {
        number -= m[s[i]];
      } else {
        number += m[s[i]];
      }
    }

    return number;
  }
};

int main() {
  cout << (new Solution())->romanToInt("LVIII") << endl;
  cout << (new Solution())->romanToInt("IV") << endl;
  cout << (new Solution())->romanToInt("MCMXCIV") << endl;

  return 0;
}
