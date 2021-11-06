#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>

using namespace std;


class Solution {
public:
  const int size = 9;
  const int subSize = 3;
  vector<vector<int>> b = vector<vector<int>>();

  bool isValidCell(int x, int y) {
    for (int i = 0; i < size; ++i) {
      if (b[x][i] == b[x][y] && y != i) {
        return false;
      }

      if (b[i][y] == b[x][y] && x != i) {
        return false;
      }
    }

    int xStart = x / subSize;
    int yStart = y / subSize;
    for (int j = xStart * 3; j < xStart * subSize + subSize; ++j) {
      for (int k = yStart * 3; k < yStart * subSize + subSize; ++k) {
        if (b[j][k] == b[x][y] && (j != x && k != y)) {
          return false;
        }
      }
    }

    return true;
  }

  bool isValidSudoku(vector<vector<char>>& board) {
    for (int i = 0; i < board.size(); ++i) {
      b.emplace_back();
      for (int j = 0; j < board[i].size(); ++j) {
        if (board[i][j] == '.') {
          b[i].push_back(0);
        }  else {
          b[i].push_back(board[i][j] - '0');
        }
      }
    }

    for (int i = 0; i < b.size(); ++i) {
      for (int j = 0; j < b[i].size(); ++j) {
        if (b[i][j] != 0 && !isValidCell(i, j)) {
          return false;
        }
      }
    }

    return true;
  }
};

int main() {

  return 0;
}
