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
  static void appendRes(string& s, int n) {
    s = (char)(n + '0') + s;
  }

  string addStrings(string num1, string num2) {
    auto n1 = vector<int>(num1.length());
    auto n2 = vector<int>(num2.length());
    for (int i = 0; i < n1.size(); ++i) n1[i] = num1[i] - '0';
    for (int i = 0; i < n2.size(); ++i) n2[i] = num2[i] - '0';

    auto numMax = n2, numMin = n1;
    if (num1.length() > num2.length()) swap(numMax, numMin);

    string res;

    int numMaxPos = numMax.size();
    int appendToNextRank = 0;
    int tmpSum;
    for (int i = numMin.size() - 1; i >= 0; --i) {
      numMaxPos--;

      tmpSum = numMin[i] + numMax[numMaxPos] + appendToNextRank;
      appendToNextRank = tmpSum / 10;
      appendRes(res, tmpSum % 10);
    }

    for (int i = numMax.size() - numMin.size() - 1; i >= 0; --i) {
      tmpSum = numMax[i] + appendToNextRank;
      appendToNextRank = tmpSum / 10;
      appendRes(res, tmpSum % 10);
    }

    if (appendToNextRank != 0) {
      appendRes(res, appendToNextRank);
    }

    return res;
  }
};


int main() {
  cout << Solution().addStrings("11", "123") << endl; // 134
  cout << Solution().addStrings("13", "129") << endl; // 142
  cout << Solution().addStrings("131", "129") << endl; // 260
  cout << Solution().addStrings("1", "2") << endl; // 3
  cout << Solution().addStrings("1", "22") << endl; // 23
  cout << Solution().addStrings("11", "2") << endl; // 13
  cout << Solution().addStrings("11", "22") << endl; // 33
  cout << Solution().addStrings("1", "9") << endl; // 10

  return 0;
}
