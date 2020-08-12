# 203. Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ret = first = ListNode(0)
        ret.next = node = head
        while node:
            if node.val == val:
                first.next = node.next
            else:
                first = node
            node = node.next
            # print(first,node)
        return ret.next
        
# Time complexity: O(N), space: (1)
