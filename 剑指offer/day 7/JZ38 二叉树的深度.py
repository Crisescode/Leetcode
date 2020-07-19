#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 15/07/20

"""
题目描述：
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        x = pRoot

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        return max(left, right) + 1


class Solution2:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        q = []
        depth = 0
        q.append(pRoot)
        while len(q):  # 队列为空时说明没有下一层
            length = len(q)
            for i in range(length):  # 遍历层的每个节点看是否有子节点有则加入
                current = q.pop(0)  # current为当前遍历到的层中节点，取出，注意pop(-1)为默认，这里要pop(0),取出第一个，先入先出
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            depth += 1
        return depth


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(Solution().TreeDepth(root))
    print(Solution2().TreeDepth(root))
