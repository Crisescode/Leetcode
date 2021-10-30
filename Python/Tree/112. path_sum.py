#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/path-sum/
# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.

"""
Example 1:
             5
          /    \
        4      8
       /     /  \
      11    13  4
    /  \    /    \
   7   2   7      1

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root and targetSum != 0:
            return False
        pass
#
#         left_vals, right_vals = [], []
#
#         def get_val_util_leaf(root, vals):
#             if root.left and not root.left.left and not root.left.right:
#                 vals.append(root.left.val)
#
#             vals.append(root.)
#
#         left_vals = get_val_util_leaf(root.left, left_vals)
#         right_vals = get_val_util_leaf(root.right, right_vals)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left.left = TreeNode(7)
    root.right.right.right = TreeNode(1)

    print(Solution().hasPathSum(root, targetSum=22))

