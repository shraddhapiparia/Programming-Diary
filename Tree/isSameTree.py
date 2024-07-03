# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [p], [q]
        while stack1 or stack2:
            n1 = stack1.pop()
            n2 = stack2.pop()
            if (n1,n2) == (None, None):
                continue
            elif not (n1 and n2):
                return False
            elif n1.val != n2.val:
                return False
            stack1.append(n1.left)
            stack1.append(n1.right)
            stack2.append(n2.left)
            stack2.append(n2.right)
        return not (stack1 and stack2)

# Using Recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
