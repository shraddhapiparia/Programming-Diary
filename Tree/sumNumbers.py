# 129. Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        stack, s = [(root,0)], 0
        if not root:
            return 0
        while stack:
            node, val = stack.pop()
            new_val = val*10 + node.val
            if not node.left and not node.right:
                s += new_val
            if node.left:
                stack.append((node.left, new_val))
            if node.right:
                stack.append((node.right, new_val))
        return s
# Time : O(N) Space: O(logN)

Approach 2: Recursion
