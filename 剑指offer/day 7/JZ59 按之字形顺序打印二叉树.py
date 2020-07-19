#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 15/07/20

"""
题目描述：
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        q = []
        res = []
        depth = 0
        q.append(pRoot)
        while q:  # 队列为空时说明没有下一层
            length = len(q)
            for i in range(length):  # 遍历层的每个节点看是否有子节点有则加入
                current = q.pop(0)  # current为当前遍历到的层中节点，取出，注意pop(-1)为默认，这里要pop(0),取出第一个，先入先出
                if depth % 2 == 0:
                    if current.left:
                        q.append(current.left)
                        res.append(current.left.val)
                    if current.right:
                        q.append(current.right)
                        res.append(current.right.val)
                else:
                    if current.left:
                        q.append(current.left)
                        res.insert(0, current.left.val)
                    if current.right:
                        q.append(current.right)
                        res.insert(0, current.right.val)

            depth += 1
        return res


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(Solution().Print(root))
