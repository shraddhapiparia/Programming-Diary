# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack1, stack2 = [root.left], [root.right]
        while stack1 and stack2:
            root1, root2 = stack1.pop(), stack2.pop()
            if (root1, root2) == (None, None):
                continue
            elif not (root1 and root2): 
                return False
            elif root1.val != root2.val:
                return False
            stack1.append(root1.right)
            stack1.append(root1.left)
            stack2.append(root2.left)
            stack2.append(root2.right)
        return not (stack1 or stack2) 

