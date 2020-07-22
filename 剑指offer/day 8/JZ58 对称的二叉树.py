#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 20/07/20

"""
题目描述：
请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        raw_tree = []
        mirror_tree = []
        # print(self.pre_travel(raw_tree, pRoot))
        root = self.mirror_tree(pRoot)
        # print(self.pre_travel(mirror_tree, root))

        return raw_tree == mirror_tree

    def mirror_tree(self, root):
        if not root:
            return None

        node = root.left
        root.left = root.right
        root.right = node

        self.mirror_tree(root.left)
        self.mirror_tree(root.right)

        return root

    def pre_travel(self, val, root):
        if root is None:
            return

        val.append(root.val)
        self.pre_travel(val, root.left)
        self.pre_travel(val, root.right)

        return val


if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(11)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(5)

    print(Solution().isSymmetrical(root))
