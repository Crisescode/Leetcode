#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.

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
           [1, 3, 2]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return

    root.left, root.right = \
        invertTree(root.right), invertTree(root.left)

    return root


# 递归方法
class ReSolution:
    def preOrderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        if root:
            res = res + [root.val]
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)

        return res

    def inOrderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        if root:
            res = res + self.inOrderTraversal(root.left)
            res = res + [root.val]
            res = res + self.inOrderTraversal(root.right)

        return res

    def postOrderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        if root:
            res = res + self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res = res + [root.val]

        return res


# 迭代方法
class Solution2:
    def preOrderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = [] # 添加右节点
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res

    def inOrderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = [] # 添加根节点
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

        return res

    def postOrderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = [] # 根据左右根 反转 根右左的特性求解
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()

        return res[::-1]


def levelOrderTraversal(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    curr, ret = [root], []
    while curr:
        ret.append([i.val for i in curr])
        curr = [kid for node in curr for kid in (node.left, node.right) if kid]
    return ret


if __name__ == "__main__":
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(7)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)
    tree1.right.left = TreeNode(6)
    tree1.right.right = TreeNode(9)

    invert_tree = invertTree(tree1)
    print("----------- 递归方法 ------------")
    print("前序遍历：", ReSolution().preOrderTraversal(invert_tree))
    print("中序遍历：", ReSolution().inOrderTraversal(invert_tree))
    print("后序遍历：", ReSolution().postOrderTraversal(invert_tree))

    print("----------- 迭代方法 -------------")
    print("前序遍历：", Solution2().preOrderTraversal(invert_tree))
    print("前序遍历：", Solution2().inOrderTraversal(invert_tree))
    print("后序遍历：", Solution2().postOrderTraversal(invert_tree))

    print("----------- 层次遍历 -------------")
    print(levelOrderTraversal(invert_tree))