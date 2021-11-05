#include <iostream>

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
  bool isPalindrome(ListNode *head) {
    auto ih = *head;
    int len = 1;
    while (head->next != nullptr) {
      len++;
      head = head->next;
    }

    auto a = new int[len];
    a[0] = ih.val;
    for (int i = 1; i < len; ++i) {
      ih = *ih.next;
      a[i] = ih.val;
    }

    int r = len - 1;
    for (int l = 0; l < len; ++l) {
      if (l == r) {break;}
      if (a[l] != a[r]) {return false;}
      r--;
    }

    return true;
  }
};

int main() {
  auto* x = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));

  cout << ((new Solution())->isPalindrome(x) ? "true" : "false") << endl;
  return 0;
}
