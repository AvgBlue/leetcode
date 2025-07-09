
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode reverseList(ListNode head) {
      if(head ==null){
        return head;
      }
      ListNode runner=head.next;
      ListNode next=null;
      ListNode pred=head;
      pred.next=null;
      while (runner!=null) {
        next=runner.next;
        runner.next=pred;
        pred=runner;
        runner=next;
      }
      return pred;
    }
}
