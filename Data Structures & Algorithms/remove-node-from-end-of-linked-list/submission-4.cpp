class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Traverse and get the length
        ListNode* current = head;
        int length = 0;
        while (current != nullptr) {
            ++length;
            current = current->next;
        }
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        current = dummy;
        for (int i = 0; i < length - n; ++i) {
            current = current->next;
        } // reach the node before the node to be deleted
        ListNode* node_to_delete = current->next; // prevent memory leak?
        current->next = current->next->next;
        delete node_to_delete;

        ListNode* new_list = dummy->next;
        delete dummy;
        return new_list;
    }
};