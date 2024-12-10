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
    ListNode? result;
    while (node1 != null && node2 != null) {
      if (node1.val < node2.val) {
        result = node1;
        node1 = node1.next;
      } else {
        result = node2;
        node2 = node2.next;
      }
      result = result.next;
    }
    return result;
  }
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}
