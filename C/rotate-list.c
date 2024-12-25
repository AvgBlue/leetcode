#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

int len = 0;
ListNode* first = NULL;
ListNode* last = NULL;

void findLastAndLen(ListNode* head) {
    last = head;
    len = 1; 
    while (last->next != NULL) {
        last = last->next;
        len++;
    }
}

ListNode* getElementAt(int index) {
    if (index >= len || index < 0) return NULL;
    ListNode* current = first;
    for (int i = 0; i < index; i++) {
        current = current->next;
    }
    return current;
}

ListNode* rotateRight(ListNode* head, int k) {
    if (head == NULL) return NULL;

    first = head;

    findLastAndLen(head);

    k %= len;
    if (len == 1 || k == 0) {
        return head;
    }

    ListNode* newLast = getElementAt(len - k - 1);
    ListNode* newHead = newLast->next;
    newLast->next = NULL;
    last->next = head;

    return newHead;
}


