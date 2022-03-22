#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/invert-binary-tree/
# Invert a binary tree.

"""
Example:
    Input:
                 4
               / \
             2    7
           / \   / \
          1   3  6  9
    Output:

                 4
               / \
             7    2
           / \   / \
          9   6  3  1
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
        if not root:
            return None

        queue = [root]
        while queue:
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return root


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    invert_tree = Solution().invertTree(tree)
    invert_tree2 = Solution2().invertTree(tree)
    print(Solution().preOrder(invert_tree))
    print(Solution().preOrder(invert_tree2))
