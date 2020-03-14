# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
            
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr1 = headA
        ptr2 = headB
        l1 = l2 = 0
        while ptr1 != None:
            l1 += 1
            ptr1 = ptr1.next
        while ptr2 != None:
            l2 += 1
            ptr2 = ptr2.next
        ptr1 = headA
        ptr2 = headB
        if l1>l2:
            for i in range(l1-l2):
                ptr1 = ptr1.next
        else:
            for i in range(l2-l1):
                ptr2 = ptr2.next
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
