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


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pass
