# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        i = 0
        while i < l-n:
            curr = curr.next
            i += 1
        # need to stop at the node before the node to be deleted
        next_node = curr.next.next
        curr.next = next_node
        return dummy.next
