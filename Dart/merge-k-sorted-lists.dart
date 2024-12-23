

class Solution {
  ListNode? mergeKLists(List<ListNode?> lists) {
    lists.removeWhere((list) => list == null);

    if (lists.isEmpty) {
      return null;
    }
    if (lists.length == 1) {
      return lists[0];
    }

    ListNode? result = ListNode(0, null);
    ListNode? runner = result;

    while (lists.length > 1) {
      ListNode? minNode = lists[0];
      int minNodeIndex = 0;
      for (int i = 0; i < lists.length; i++) {
        if (lists[i]!.val < minNode!.val) {
          minNode = lists[i];
          minNodeIndex = i;
        }
      }
      runner!.next = minNode;
      runner = runner.next;
      lists[minNodeIndex] = lists[minNodeIndex]!.next;
      if (lists[minNodeIndex] == null) {
        lists.removeAt(minNodeIndex);
      }
    }
    runner!.next = lists[0];
    return result.next;
  }

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
    return result.next;
  }
}

class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

void main() {
  List<ListNode?> lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
  ];

  Solution solution = Solution();
  ListNode? mergedList = solution.mergeKLists(lists);

  List<int> result = [];
  while (mergedList != null) {
    result.add(mergedList.val);
    mergedList = mergedList.next;
  }
  print(result);
}
