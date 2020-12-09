1586. Binary Search Tree Iterator II

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#    int next() Moves the pointer to the right, then returns the number at the pointer.
#    boolean hasPrev() Returns true if there exists a number in the traversal to the left of the pointer, otherwise returns false.
#    int prev() Moves the pointer to the left, then returns the number at the pointer.

# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() and prev() calls will always be valid. That is, there will be at least a next/previous number in the in-order traversal when next()/prev() is called.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res, stack, self.idx = [], [(root, False)], -1
        while stack:
            node, flag = stack.pop()
            if node:
                if not flag:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
                else:
                    self.res.append(node.val)

    def hasNext(self) -> bool:
        return self.idx < len(self.res) - 1
        

    def next(self) -> int:
        self.idx += 1
        return self.res[self.idx]
        

    def hasPrev(self) -> bool:
        return self.idx > 0
        

    def prev(self) -> int:
        self.idx -= 1
        return self.res[self.idx]
