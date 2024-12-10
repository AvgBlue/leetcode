/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  ListNode? removeNthFromEnd(ListNode? head, int n) {
    if (head == null) {
      return null;
    }

    ListNode? frontLine = head;
    ListNode? backLine = head;
    for (int i = 0; i < n; i++) {
      frontLine = frontLine?.next;
    }
    while (frontLine?.next != null) {
      frontLine = frontLine?.next;

      backLine = backLine?.next;
    }
    backLine?.next = backLine?.next?.next;
    return head;
  }
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

void main() {
  // Helper function to create a linked list from a list of values
  ListNode? createLinkedList(List<int> values) {
    if (values.isEmpty) return null;
    ListNode head = ListNode(values[0]);
    ListNode current = head;
    for (int i = 1; i < values.length; i++) {
      current.next = ListNode(values[i]);
      current = current.next!;
    }
    return head;
  }

  // Helper function to convert the linked list to a list of values
  List<int> linkedListToList(ListNode? head) {
    List<int> result = [];
    ListNode? current = head;
    while (current != null) {
      result.add(current.val);
      current = current.next;
    }
    return result;
  }

  // Test case
  ListNode? head = createLinkedList([1, 2, 3, 4, 5]);
  int n = 2;

  Solution solution = Solution();
  ListNode? newHead = solution.removeNthFromEnd(head, n);

  print("Linked list after removing $n-th node from the end:");
  print(linkedListToList(newHead));
}
