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
            return []

        depth = 0
        node_queue = [pRoot]
        res = []

        while node_queue:
            val = []
            length = len(node_queue)
            for i in range(length):
                current = node_queue.pop(0)
                val.append(current.val)

                if current.left:
                    node_queue.append(current.left)

                if current.right:
                    node_queue.append(current.right)

            if depth % 2 == 0:
                res.append(val)
            else:
                res.append(list(reversed(val)))

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
