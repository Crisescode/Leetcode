#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.

"""
Example:
    Input:
                 1
                 \
                 2
                /
              3
    Output:
           [1, 3, 2]
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def invertTree(self, root: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return

        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)

        return root

    def preOrder(self, root):
        if root is None:
            return

        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


# 迭代
class Solution2:
    def invertTree(self, root: TreeNode) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(7)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)
    tree1.right.left = TreeNode(6)
    tree1.right.right = TreeNode(9)

    invert_tree = Solution().invertTree(tree1)
    print(Solution().preOrder(invert_tree))
