# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, level, levels = deque([root,]), 0, []
        while queue:
            levels.append([])
            for i in range(len(queue)):
                n = queue.popleft()
                levels[level].append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            print(level,levels[level])
            level += 1
        return levels
