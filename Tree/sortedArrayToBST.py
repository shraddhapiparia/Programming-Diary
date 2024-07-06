# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        n = len(nums)
        root = TreeNode()
        stack = [(0,n,root)]
        while stack:
            i, j, node = stack.pop()
            mid = (i+j)//2
            node.val = nums[mid]
            if mid > i:
                node.left= TreeNode()
                stack.append((i,mid,node.left))
            if mid+1 < j:
                node.right = TreeNode()
                stack.append((mid+1,j,node.right))
        return root

#USING RECURSION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
