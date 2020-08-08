# 83. Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        first, second = head, head.next
        while second:
            if first.val == second.val:
                first.next = second.next
            else:
                first = first.next
            second = second.next
        return head

