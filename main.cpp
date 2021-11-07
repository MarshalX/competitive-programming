#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>

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
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (l1 == nullptr) {
      return l2;
    }
    if (l2 == nullptr) {
      return l1;
    }

    ListNode* res = nullptr;
    ListNode* start = nullptr;
    while (l1 != nullptr && l2 != nullptr) {
      auto* tmp = new ListNode(l1->val <= l2->val ? l1->val : l2-> val);

      if (res == nullptr) {
        start = tmp;
      } else {
        res->next = tmp;
      }
      res = tmp;

      if (l1->val <= l2->val) {
        l1 = l1->next;
      } else {
        l2 = l2->next;
      }
    }

    if (l1 != nullptr) {
      res->next = l1;
    }
    if (l2 != nullptr) {
      res->next = l2;
    }

    return start;
  }
};

int main() {
  auto* l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
  auto* l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
  auto* res = Solution().mergeTwoLists(l1, l2);
  while (res != nullptr) {
    cout << res->val << " ";
    res = res->next;
  }

  return 0;
}
