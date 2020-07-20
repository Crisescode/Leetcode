#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 20/07/20

"""
题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

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

            res.append(val)

        return res


if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)

    print(Solution().Print(root))
