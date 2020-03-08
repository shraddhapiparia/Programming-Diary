# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque([(root,1)])
        depth = 0
        if not root:
            return 0
        while queue:
            n,depth = queue.popleft()
            if not n.left and not n.right:
                return depth
            if n.left:
                queue.append((n.left, depth+1))
            if n.right:
                queue.append((n.right, depth+1))
