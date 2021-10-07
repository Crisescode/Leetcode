#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""
Example:
    Input:
                 1
                 \
                 2
                /
              3
    Input: root = [1, null, 2, 3]
    Output:
           [1, 2, 3]
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代1
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res


# 迭代2
class Solution2:
    def preorderTraversal(self, root):
        if root is None:
            return []

        res, stack = [], []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res


# 递归1
class Solution3:
    def preorderTraversal(self, root):
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# 递归2
class Solution4:
    def preorderTraversal(self, root):
        result = []

        def traversal(root: TreeNode):
            if root is None:
                return

            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(5)
    tree.right.left = TreeNode(3)
    tree.left.right = TreeNode(10)
    tree.right.right = TreeNode(20)

    print(Solution().preorderTraversal(tree))
    print(Solution2().preorderTraversal(tree))
    print(Solution3().preorderTraversal(tree))
    print(Solution4().preorderTraversal(tree))
