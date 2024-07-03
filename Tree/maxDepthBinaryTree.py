# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack, maxval = [(root,1)], 0
        depth = 0
        if not root:
            return 0
        while stack:
            n,depth = stack.pop()
            maxval = depth if depth > maxval else maxval
            if n.left:
                stack.append((n.left, depth+1))
            if n.right:
                stack.append((n.right, depth+1))
        return maxval

# Using recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
