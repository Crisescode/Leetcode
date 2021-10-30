#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/find-bottom-left-tree-value/
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

"""
Example 1:
           1
         /  \
        2    3
       /   /  \
      4   5   6
         /
        7

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> (List, int):
        if not root:
            return 0

        from collections import deque
        queue = deque([root])
        results = []

        while queue:
            length = len(queue)
            res = []
            for _ in range(length):
                cur = queue.popleft()
                res.append(cur.val)

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            results.append(res)

        return results, results[-1][0]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)

    print(Solution().findBottomLeftValue(root))
