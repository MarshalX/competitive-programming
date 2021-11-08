#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>

using namespace std;


struct ListNode {
   int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
  void deleteNode(ListNode* node) {
    ListNode* prev = node;
    bool isFirst = true;
    while (node->next != nullptr) {
      if (!isFirst) {
        prev = prev->next;
      } else {
        isFirst = false;
      }

      node->val = node->next->val;
      node = node->next;
    }
    prev->next = nullptr;
  }
};

int main() {
  auto* h = new ListNode(4, new ListNode(5, new ListNode(1, new ListNode(9))));
  Solution().deleteNode(h->next);
  while (h != nullptr) {
    cout << h->val << " ";
    h = h->next;
  }

  return 0;
}
