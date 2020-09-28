#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
"""
For example, this binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric:
    Symmetric tree:
                 1
               / \
             2    2
           / \   / \
          3  4  4  3
    But the following [1, 2, 2, null, 3, null, 3] is not:

                 1
               / \
             2    2
             \     \
              3     3
"""
from Utils.timer_decorater import timer


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @timer
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        import collections
        queue = collections.deque()
        queue.append((root, root))

        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


if __name__ == "__main__":
    pass
