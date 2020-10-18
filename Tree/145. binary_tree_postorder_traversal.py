#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

"""
Example:
    Input:
                 1
                 \
                 2
                /
              3
    Input: root = [1, null, 2, 3]
    Output:
           [3, 2, 1]
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return res[::-1]


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(5)
    tree.right.left = TreeNode(3)
    tree.left.right = TreeNode(10)
    tree.right.right = TreeNode(20)

    print(Solution().postorderTraversal(tree))
