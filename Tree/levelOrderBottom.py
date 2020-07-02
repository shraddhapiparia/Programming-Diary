107. Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

# return its bottom-up level order traversal as: [  [15,7],  [9,20],  [3]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        dicti = {}
        stack = [(root,0)]
        ans = []
        while stack:
            (node, level) = stack.pop()
            if level in dicti:
                dicti[level].append(node.val)
            else:
                dicti[level] = [node.val]
            if node.right:
                stack.append((node.right,level+1))
            if node.left:
                stack.append((node.left,level+1))
        for key,val in reversed(dicti.items()):
            ans.append(val)
        return ans
        
# Time O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])
        
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])
            
            for node in curr_level:
                # append the current node value
                levels[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        return levels[::-1]
