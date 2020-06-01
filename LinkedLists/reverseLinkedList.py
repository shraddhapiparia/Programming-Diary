class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        first, dummy = head, None
        while first:
            temp = first.next
            first.next = dummy
            dummy = first
            first = temp
        return dummy
