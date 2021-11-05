#include <iostream>
#include <vector>

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
  vector<int> values = vector<int>();

  ListNode* getNextNode(int n) {
    if (n != values.size()) {
      return new ListNode(values[n], getNextNode(n + 1));
    } else {
      return nullptr;
    }
  }

  ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
      return head;
    }

    while (true) {
      values.push_back(head->val);
      if (head->next == nullptr) {
        break;
      }
      head = head->next;
    }

    reverse(values.begin(), values.end());

    return getNextNode(0);
  }
};

int main() {
  auto* x = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
  auto* r = (new Solution())->reverseList(x);

  while (true) {
    cout << r->val << endl;
    if (r->next == nullptr) {break;}
    r = r->next;
  }

  return 0;
}
