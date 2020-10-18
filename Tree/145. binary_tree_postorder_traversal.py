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
        pass
