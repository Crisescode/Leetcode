#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to
# the farthest leaf node.
# Note: A leaf is a node with no children.
#
"""
For example, given a binary tree [3, 9, 3, 4, 5, null, null]:
                 3
               / \
             9    3
           / \
          4  5

Return its depth = 3.
"""
from Utils.timer_decorater import timer


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS: 深度遍历
class Solution:
    @timer
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0

            return max(1 + dfs(root.left), 1 + dfs(root.right))

        return dfs(root)


# BFS：层次遍历
class Solution2:
    @timer
    def maxDepth(self, root: TreeNode) -> int:
        def bfs(root: TreeNode) -> int:
            if root is None:
                return 0

            level, ret = [root], []
            while level:
                ret.append([item.val for item in level])
                level = [kid for node in level for kid in (node.left, node.right) if kid]

            return len(ret)

        return bfs(root)


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    print(Solution().maxDepth(tree))
    print(Solution2().maxDepth(tree))
