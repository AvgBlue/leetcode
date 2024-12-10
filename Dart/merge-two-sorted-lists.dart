class Solution {
  ListNode? mergeTwoLists(ListNode? list1, ListNode? list2) {
    if (list1 == null) {
      return list2;
    }
    if (list2 == null) {
      return list1;
    }
    ListNode? node1 = list1;
    ListNode? node2 = list2;
    ListNode result = ListNode(0, null);
    ListNode runner = result;

    while (node1 != null && node2 != null) {
      if (node1.val < node2.val) {
        runner.next = node1;
        node1 = node1.next;
      } else {
        runner.next = node2;
        node2 = node2.next;
      }
      runner = runner.next!;
    }
    if (node1 == null) {
      runner.next = node2;
    } else {
      runner.next = node1;
    }
    return result;
  }
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}
