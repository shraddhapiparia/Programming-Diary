# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #node, s = root, sum
        stack = [(root,sum)]
        if not root:
            return False
        while stack:
            node, s = stack.pop()
            rem = s - node.val
            if rem == 0 and not node.left and not node.right:
                return True
            if node.left:
                stack.append((node.left,rem))
            if node.right:
                stack.append((node.right,rem))
        return False


Time and space complexity: O(N)
