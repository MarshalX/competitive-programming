#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>

using namespace std;


class Solution {
public:
  map<int, char> m = map<int, char>{
      {1000, 'M'},
      {500, 'D'},
      {100, 'C'},
      {50, 'L'},
      {10, 'X'},
      {5, 'V'},
      {1, 'I'},
  };

  map<int, string> exc = map<int, string>{
    {4, "IV"},
    {40, "XL"},
    {400, "CD"},

    {9, "IX"},
    {90, "XC"},
    {900, "CM"},
  };

  string intToRoman(int num) {
    string s = to_string(num);
    vector<string> resParts = {"", "", "", ""};

    for (int i = s.length() - 1; i >= 0; --i) {
      int n = s[i] - '0';
      int rank = s.length() - i - 1;
      int e = pow(10, rank);

      int nn = n * e;
      if (exc.find(nn) != exc.end()) {
        resParts[i] = exc[nn];
      } else {
        string tmp = "";
        int da = nn;
        for (auto p = m.rbegin(); p != m.rend(); ++p) {
          if (da >= p->first) {
            int k = da / p->first;
            da -= p->first * k;
            for (int j = 0; j < k; ++j) {
              tmp += p->second;
            }
          }
        }

        resParts[i] = tmp;
      };
    }

    stringstream ss;
    ss << resParts[0] << resParts[1] << resParts[2] << resParts[3];
    return ss.str();
  }
};

int main() {
  cout << (new Solution())->intToRoman(1) << endl; // II
  cout << (new Solution())->intToRoman(2) << endl; // II
  cout << (new Solution())->intToRoman(3) << endl; // III
  cout << (new Solution())->intToRoman(58) << endl; // LVIII
  cout << (new Solution())->intToRoman(4) << endl; // IV
  cout << (new Solution())->intToRoman(1994) << endl; // MCMXCIV
  cout << (new Solution())->intToRoman(2994) << endl; // MMCMXCIV
  cout << (new Solution())->intToRoman(3594) << endl; // MMMDXCIV

  return 0;
}
