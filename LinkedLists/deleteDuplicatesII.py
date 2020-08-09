# 82. Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        ret = pre = ListNode(0)
        ret.next = cur = head
        while(cur.next):
            nxt = cur.next
            if cur.val == nxt.val:
                while(nxt.next and nxt.val == nxt.next.val):
                    nxt = nxt.next
                pre.next = cur = nxt.next
                if not cur: return ret.next
            else:
                pre,cur,nxt = cur,nxt,nxt.next
            
            
        return ret.next

