#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 09/07/20

"""
题目描述：
操作给定的二叉树，将其变换为源二叉树的镜像。

Example:
  二叉树的镜像定义：源二叉树
             8
           /  \
          6   10
         / \  / \
        5  7 9 11

        镜像二叉树
             8
           /  \
          10   6
         / \  / \
        11 9 7  5

时间复杂度： O(n)
空间复杂度： O(n)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return

        root.left, root.right = \
            self.Mirror(root.right), self.Mirror(root.left)

        return root

    def preOrder(self, root):
        if root is None:
            return

        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    tree1 = TreeNode(8)
    tree1.left = TreeNode(6)
    tree1.right = TreeNode(10)
    tree1.left.left = TreeNode(5)
    tree1.left.right = TreeNode(7)
    tree1.right.left = TreeNode(9)
    tree1.right.right = TreeNode(11)

    invert_tree = Solution().Mirror(tree1)
    print(Solution().preOrder(invert_tree))
