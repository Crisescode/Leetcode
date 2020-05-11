#! /usr/bin/env python
# -*- coding: utf-8 -*-


# https://leetcode-cn.com/problems/merge-two-binary-trees/
# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise,
# the NOT null node will be used as the node of new tree.
#
"""
Example:
    Input:
              Tree 1                 Tree2
                 1                     2
               / \                    / \
             3    2                  1   3
           /                         \    \
         5                            4    7
    Output:
    Merged tree:
                          3
                         / \
                       4    5
                      / \    \
                    5    4    7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

