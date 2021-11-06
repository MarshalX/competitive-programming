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

  vector<int> getAvailable(int x, int y) {
    vector<int> avail = vector<int>(10);
    fill(avail.begin(), avail.end(), 0);
    avail[0] = 1;

    for (int i = 0; i < size; ++i) {
      avail[b[x][i]] = 1;
      avail[b[i][y]] = 1;
    }

    int xStart = x / subSize;
    int yStart = y / subSize;
    for (int j = xStart * 3; j < xStart * subSize + subSize; ++j) {
      for (int k = yStart * 3; k < yStart * subSize + subSize; ++k) {
        avail[b[j][k]] = 1;
      }
    }

    return avail;
  }

  bool solver(int x, int y) {
    if ((x == size - 1) && (y == size)) {
      return true;
    }

    if (y == size) {
      y = 0;
      x += 1;
    }

    if (b[x][y] == 0) {
      auto avail = getAvailable(x, y);
      for (int i = 1; i < 10 ; ++i) {
        if (avail[i] == 0) {
          b[x][y] = i;
          if (solver(x, y + 1)) {
            return true;
          }
        }
      }

      b[x][y] = 0;
      return false;
    }

    return solver(x, y + 1);
  }

  void solveSudoku(vector<vector<char>>& board) {
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

    solver(0, 0);

    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[i].size(); ++j) {
        board[i][j] = b[i][j] + '0';
      }
    }
  }
};

int main() {

  return 0;
}
