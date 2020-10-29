#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
#
"""
For example, given the following tree:
                 1
               / \
             2    5
           / \    \
          3  4    6
The flattened tree should look like:
1 -> 2 -> 3 -> 4 -> 5 -> 6
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        vals, stack = [], [root]
        if stack is not None:
            vals.append(root.val)
            root = root.left
            stack.append(root.right)
        else:
            stack



if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(6)

    print(Solution().flatten(tree))
