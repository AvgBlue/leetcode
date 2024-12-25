// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  int len = 0;
  ListNode? first = null;
  ListNode? last = null;

  ListNode? rotateRight(ListNode? head, int k) {
    first = head;
    findLastAndLen(head);
    k %= len;
    ListNode? newLast = getElementAt(len - k);
    ListNode? newHead = newLast!.next;
    newLast.next = null;
    last!.next = head;
    return newHead;
  }

  void findLastAndLen(ListNode? head) {
    last = head;
    while (last?.next != null) {
      last = last?.next;
      len++;
    }
    len++;
  }

  ListNode? getElementAt(int index) {
    if (index >= len || index < 0) return null;
    ListNode? current = first;
    for (int i = 0; i < index; i++) {
      current = current?.next;
    }
    return current;
  }
}
