/**
 * Definition for singly-linked list.
 */
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    return help(l1, l2, 0);
  }

  ListNode? help(ListNode? l1, ListNode? l2, int carry) {
    if (l1 == null && l2 == null) {
      return carry == 0 ? null : ListNode(carry);
    }
    if (l1 == null) {
      return help(l2, ListNode(carry), 0);
    }
    if (l2 == null) {
      return help(l1, ListNode(carry), 0);
    }
    int sum = l1.val + l2.val + carry;
    print(sum % 10);
    ListNode? next = help(l1.next, l2.next, sum ~/ 10);
    return ListNode(sum % 10, next);
  }

  void printList(ListNode? node) {
    while (node != null) {
      print(node.val);
      node = node.next;
    }
  }
}

void main() {
  Solution solution = Solution();

  // Create first number: 342 (represented as 2 -> 4 -> 3)
  ListNode l1 = ListNode(2, ListNode(4, ListNode(3)));

  // Create second number: 465 (represented as 5 -> 6 -> 4)
  ListNode l2 = ListNode(5, ListNode(6, ListNode(4)));

  // Add the two numbers
  ListNode? result = solution.addTwoNumbers(l1, l2);
  print("result: \n");
  // Print the result: 807 (represented as 7 -> 0 -> 8)
  solution.printList(result);
}
