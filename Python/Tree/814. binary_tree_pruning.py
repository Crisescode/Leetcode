#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-pruning/
# Given the root of a binary tree, return the same tree where every subtree (of the given tree)
# not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.
#

"""
Example 1:

    Input: s = "abcde", goal = "cdeab"
    Output: true

Example 2:

    Input: s = "abcde", goal = "abced"
    Output: false
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        pass


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass
