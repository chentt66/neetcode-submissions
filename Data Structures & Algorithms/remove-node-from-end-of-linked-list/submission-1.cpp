/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int l = 0;
        ListNode* current = head;
        while (current != nullptr) {
            ++l;
            current = current->next;
        }
        int i = 0;
        ListNode* dummy = new ListNode(-1, head);
        current = dummy;
        while (i < l-n) {
            current = current->next;
            i += 1;
        }
        ListNode* node_to_delete = current->next;
        current->next = current->next->next;
        return dummy->next;
    }
};
