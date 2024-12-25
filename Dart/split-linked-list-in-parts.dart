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
  int getLength(ListNode? head) {
    int length = 0;
    ListNode? current = head;
    while (current != null) {
      length++;
      current = current.next;
    }
    return length;
  }

  List<ListNode?> splitListToParts(ListNode? head, int k) {
    int len = getLength(head);
    List<ListNode?> result = List.filled(k, null);
    List<int> resultLen = List.filled(k, 0);
    for (int i = 0; i < len; i++) {
      resultLen[i % k]++;
    }
    ListNode? runner = head;
    for (int i = 0; i < k; i++) {
      result[i] = runner;
      for (int j = 0; j < resultLen[i] - 1; j++) {
        runner = runner!.next;
      }
      if (resultLen[i] == 0) continue;
      ListNode? temp = runner;
      runner = runner!.next;
      temp!.next = null;
    }
    return result;
  }
}
