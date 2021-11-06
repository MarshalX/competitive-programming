#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>

using namespace std;


class UndergroundSystem {
public:
  map<string, pair<int, int>> timeDB;
  map<int, pair<string, int>> userDB;

  UndergroundSystem() {

  }

  void checkIn(int id, string stationName, int t) {
    userDB[id] = {stationName, t};
  }

  void checkOut(int id, string stationName, int t) {
    string key = userDB[id].first + "_" + stationName;
    if (timeDB.find(key) == timeDB.end()) {
      timeDB[key] = {t - userDB[id].second, 1};
    } else {
      timeDB[key] = {
          timeDB[key].first + t - userDB[id].second,
          timeDB[key].second + 1
      };
    }
    userDB.erase(id);
  }

  double getAverageTime(string startStation, string endStation) {
    string key = startStation + "_" + endStation;
    return (double)timeDB[key].first / timeDB[key].second;
  }
};

int main() {

  return 0;
}
