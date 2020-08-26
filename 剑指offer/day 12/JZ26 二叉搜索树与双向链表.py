#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 11/08/20

"""
题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，
只能调整树中结点指针的指向。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return

        nodes = []
        print(self.InOrder(pRootOfTree, nodes))

    def InOrder(self, root, nodes):
        if root is None:
            return

        self.InOrder(root.left, nodes)
        nodes.append(root.val)
        self.InOrder(root.right, nodes)

        return nodes


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)
    tree1.right.left = TreeNode(7)
    tree1.right.right = TreeNode(8)

    Solution().Convert(tree1)
