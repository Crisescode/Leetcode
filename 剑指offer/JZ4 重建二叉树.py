#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 09/07/20

"""
题目描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中
都不含重复的数字。例如输入前序遍历序列[1,2,4,7,3,5,6,8]和中序遍历序列[4,7,2,1,5,3,8,6]，
则重建二叉树并返回。

时间复杂度： O(n)
空间复杂度： O(n)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None

        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)

        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])

        return root

    def preOrder(self, root):
        if root is None:
            return

        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def InOrder(self, root):
        if root is None:
            return
        self.InOrder(root.left)
        print(root.val, end=' ')
        self.InOrder(root.right)

    def BackOrder(self, root):
        if root is None:
            return
        self.BackOrder(root.left)
        self.BackOrder(root.right)
        print(root.val, end=' ')


if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]

    reTree = Solution().reConstructBinaryTree(pre, tin)
    print("前序遍历：")
    Solution().preOrder(reTree)
    print("\n")
    print("中序遍历：")
    Solution().InOrder(reTree)
    print("\n")
    print("后序遍历：")
    Solution().BackOrder(reTree)
