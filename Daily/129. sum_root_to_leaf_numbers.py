#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 29/10/2020

# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.
#
"""
For example:

    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.

    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.

"""
from Utils.timer_decorater import timer


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@timer
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []

        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                res.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res

