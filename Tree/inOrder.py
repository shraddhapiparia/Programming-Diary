# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [(root, False)], []
        if not root:
            return ans
        while stack:
            n, flag = stack.pop()
            if n:
                if not flag:
                    stack.append((n.right,False))
                    stack.append((n, True))
                    stack.append((n.left, False))
                else:
                    ans.append(n.val)
        return ans
