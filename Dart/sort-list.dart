/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  int listLen(ListNode? head) {
    int length = 0;
    ListNode? current = head;
    while (current != null) {
      length++;
      current = current.next;
    }
    return length;
  }

  ListNode? splitInTheMiddle(ListNode? head) {
    if (head == null || head.next == null) return head;

    ListNode? slow = head;
    ListNode? fast = head;
    ListNode? prev = null;

    while (fast != null && fast.next != null) {
      prev = slow;
      slow = slow!.next;
      fast = fast.next!.next;
    }

    if (prev != null) {
      prev.next = null;
    }

    return slow;
  }

  ListNode? mergeTwoLists(ListNode? l1, ListNode? l2) {
    ListNode dummy = ListNode(0);
    ListNode current = dummy;

    while (l1 != null && l2 != null) {
      if (l1.val < l2.val) {
        current.next = l1;
        l1 = l1.next;
      } else {
        current.next = l2;
        l2 = l2.next;
      }
      current = current.next!;
    }

    if (l1 != null) {
      current.next = l1;
    } else {
      current.next = l2;
    }

    return dummy.next;
  }

  ListNode? sortList(ListNode? head) {
    if (head == null) {
      return null;
    }
    if (head.next == null) {
      return head;
    }

    ListNode? firstHalf = head;
    ListNode? secondHalf = splitInTheMiddle(head);

    ListNode? list1 = sortList(firstHalf);

    ListNode? list2 = sortList(secondHalf);

    return mergeTwoLists(list1, list2);
  }
}

void main() {
  ListNode node4 = ListNode(3);
  ListNode node3 = ListNode(1, node4);
  ListNode node2 = ListNode(2, node3);
  ListNode node1 = ListNode(4, node2);

  Solution solution = Solution();
  ListNode? sortedList = solution.sortList(node1);

  ListNode? current = sortedList;
  while (current != null) {
    print(current.val);
    current = current.next;
  }
}
