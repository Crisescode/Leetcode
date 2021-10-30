#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/sum-of-left-leaves/
# Given the root of a binary tree, return the sum of all left leaves.

"""
Example 1:
           3
         /  \
        9   20
           /  \
          15  7

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右

        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val

        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum


class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> (List, int):
        if not root:
            return 0

        stack = [root]
        res = []
        sum = 0

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.left and not cur.left.left and not cur.left.right:
                sum += cur.left.val

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return res, sum


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().sumOfLeftLeaves(root))
    print(Solution2().sumOfLeftLeaves(root))
