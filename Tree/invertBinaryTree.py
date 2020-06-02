#226. Invert a binary tree. Like Mirror image.


# Solution 1 : long version but good speed and memory
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                temp = node.left
                node.left = node.right 
                node.right = temp
                stack.append(node.left)
                stack.append(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                stack.append(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                stack.append(node.left)
        return root

# Solution 2 : Short version but takes more time
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
