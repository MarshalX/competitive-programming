#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#include <stack>
#include <queue>

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
  ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
      return head;
    }

    ListNode* next = nullptr;
    while (head != nullptr) {
      auto tmp = head->next;
      head->next = next;
      next = head;
      head = tmp;
    }

    return next;
  }
};


int main() {
  auto r = Solution().reverseList(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4)))));
  while (r != nullptr) {
    cout << r->val << " ";
    r = r->next;
  }

  return 0;
}
