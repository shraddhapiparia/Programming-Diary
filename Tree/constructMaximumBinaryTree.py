# 654. Maximum Binary Tree
# ou are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.
# Example 2:
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = TreeNode(0) 
        l, r = 0, len(nums) - 1
        nodes = [(root, l, r)]
        lut = {nums[i]: i for i in range(len(nums))}
        while nodes:
            currNode, l, r = nodes.pop()
            if l > r:
                continue
            max_index = lut[max(nums[l:r + 1])]
            currNode.val = nums[max_index]
            if l <= max_index - 1:
                currNode.left = TreeNode(0) 
                nodes.append((currNode.left, l, max_index - 1))
            if max_index + 1 <= r:
                currNode.right = TreeNode(0) 
                nodes.append((currNode.right, max_index + 1, r))
        return root


# Using Recursion
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_index = nums.index(max(nums))
        root = TreeNode(val=nums[max_index])

        root.left = self.constructMaximumBinaryTree(nums[:max_index])  # Elements to the left of max
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])  # Elements to the right of max

        return root
