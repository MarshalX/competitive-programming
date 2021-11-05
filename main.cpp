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
  ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
      return head;
    }

    vector<int> values = vector<int>();
    while (true) {
      values.push_back(head->val);
      if (head->next == nullptr) {
        break;
      }
      head = head->next;
    }

    reverse(values.begin(), values.end());

    auto* first = new ListNode(values[0]);
    auto* prev = first;
    for (int i = 1; i < values.size(); ++i) {
      auto* tmp = new ListNode(values[i]);
      prev->next = tmp;
      prev = tmp;
    }

    return first;
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
