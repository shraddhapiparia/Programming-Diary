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
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]

        parent = {root: None}
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)

        def find_ancestors(node):
            ancestors = {}
            level = 1
            while node:
                ancestors[node] = level  # Store the node itself as the key
                level += 1
                node = parent[node]
            return ancestors

        common_ancestors = find_ancestors(nodes[0])

        for node in nodes[1:]:
            current_ancestors = find_ancestors(node)
            common_ancestors = {key: common_ancestors[key] for key in common_ancestors if key in current_ancestors}

        ancestors_list = find_ancestors(nodes[0])

        for ancestor, level in sorted(ancestors_list.items(), key=lambda x: x[1], reverse=False):
            if ancestor in common_ancestors:
                return ancestor

        return None
      # Above code very slow; work on recursive solution
