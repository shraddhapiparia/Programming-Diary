# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack , res = [(root, False)], []
        if not root:
            return None
        while stack:
            n, flag = stack.pop()
            if n:
                if not flag:
                    stack.append((n, True))
                    stack.append((n.right, False))
                    stack.append((n.left, False))
                else:
                    res.append(n.val)
        return res
