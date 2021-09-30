# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def buildTree(pstart, pend, istart, iend) -> TreeNode:
            if pstart > pend:
                return None
            # locate root value and root index
            root_value = preorder[pstart]
            root = TreeNode(root_value)
            root_index = d[root_value]
            # recursively build left tree
            root.left = buildTree(pstart + 1, pstart +
                                  root_index - istart, istart, root_index - 1)
            # recursively build right tree
            root.right = buildTree(
                pstart + root_index - istart + 1, pend, root_index + 1, iend)
            return root

        if len(preorder) == 0:
            return None
        # nice method to get element index in list
        d = {j: i for i, j in enumerate(inorder)}
        n = len(preorder)
        return buildTree(0, n-1, 0, n-1)

# Time: O(n)
# space: O(n) (dict)
# (n is number of nodes in the tree)
