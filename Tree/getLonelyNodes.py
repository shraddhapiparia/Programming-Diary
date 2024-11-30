# 1469. Find All The Lonely Nodes
# In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.
# Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

# Example 1:

# Input: root = [1,2,3,null,4]
# Output: [4]
# Explanation: Light blue node is the only lonely node.
# Node 1 is the root and is not lonely.
# Nodes 2 and 3 have the same parent and are not lonely.
# Example 2:

# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
# Output: [6,2]
# Explanation: Light blue nodes are lonely nodes.
# Please remember that order doesn't matter, [2,6] is also an acceptable answer.
# Example 3:

# Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
# Output: [77,55,33,66,44,22]
# Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
# All other nodes are lonely.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely_nodes = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and not curr.right:
                lonely_nodes.append(curr.left.val)
                stack.append(curr.left)
            elif curr.right and not curr. left:
                lonely_nodes.append(curr.right.val)
                stack.append(curr.right)
            else:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return lonely_nodes

# SImilar to above with less ifs:
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        stack, lonely_nodes = [root],[]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                stack.append(curr.left)
                stack.append(curr.right)
            elif curr.left:
                lonely_nodes.append(curr.left.val)
                stack.append(curr.left)
            elif curr.right:
                lonely_nodes.append(curr.right.val)
                stack.append(curr.right)
        return lonely_nodes

# RECURSIVE SOLUTION
class Solution:
    def dfs(self,node):
            if node.left and not node.right:
                self.lonely_nodes.append(node.left.val)
            if node.right and not node.left:
                self.lonely_nodes.append(node.right.val)
            if node.left:
                self.dfs(node.left)
            if node.right:
                self.dfs(node.right)
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.lonely_nodes = []
        self.dfs(root)
        return self.lonely_nodes
