# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = curr = head
        for i in range(n):
            curr = curr.next
        if not curr:
            return prev.next
        while curr.next:
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return head
# Remove Nth Node From End of List. Given a linked list, remove the n-th node from the end of list and return its head. Follow up:

# Could you do this in one pass?
