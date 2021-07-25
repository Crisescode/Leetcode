#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Given a binary tree, return the level order traversal of its nodes' values
# (ie, from left to right, level by level).

"""
Example:
    Input:
                3
               / \
              9   20
                 / \
                15  7
    Input: root = [3, 9, 20, null, null. 15, 7]
    Output:
           [[3], [9, 20], [15, 7]]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> List[int]:
        pass
