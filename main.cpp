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
  ListNode* removeElements(ListNode* head, int val) {
    ListNode* start = nullptr;
    ListNode* res = nullptr;

    if (head == nullptr) {
      return res;
    }

    while (head != nullptr) {
      if (head->val != val) {
        if (res == nullptr) {
          start = res = new ListNode(head->val);
        } else {
          res->next = new ListNode(head->val);
          res = res->next;
        }
      }

      head = head->next;
    }

    return start;
  }
};

int main() {
  auto* h = new ListNode(1, new ListNode(2, new ListNode(6, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6)))))));
  auto* r = Solution().removeElements(h, 6);
  while (r != nullptr) {
    cout << r->val << " ";
    r = r->next;
  }

  return 0;
}
