# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        curr, length = head, 0
        while curr != None:
            length, curr = length + 1, curr.next
        mid = length// 2 
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr
 
# Approach 2 with more runtime but solution looks efficient
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# Given a non-empty, singly linked list with head node head, return a middle node of linked list. If there are two middle nodes, return the second middle node.
