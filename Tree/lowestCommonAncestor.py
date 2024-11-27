# 1676. Lowest Common Ancestor of a Binary Tree IV
# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
# Output: 1
# Explanation: The lowest common ancestor of a single node is the node itself.

# Example 3:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
# Output: 5
# Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findAncestors(self, parent, node) -> Dict['TreeNode', int]:
        ancestors, level = {}, 1
        while node:
            ancestors[node] = level
            level += 1
            node = parent[node]
        return ancestors

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        # Create parent dictionary to reference later    
        parent, stack = {root: None}, [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        # Find all ancestors of first node in nodes and store common ones in common_ancestors
        common_ancestors = self.findAncestors(parent, nodes[0])
        for node in nodes[1:]:
            node_ancestor = self.findAncestors(parent, node)
            common_ancestors = {key: common_ancestors[key] for key in common_ancestors if key in node_ancestor}

        # Return the lowest common ancestor by level
        return min(common_ancestors, key=common_ancestors.get)
