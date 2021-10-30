#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
# tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#

"""
Example 1:
             3
          /    \
        9      20
             /  \
            15  7


Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

"""

from typing import List, Union


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Union[None, TreeNode]:
        # 第一步：特征
        if not preorder:
            return None

        # 第二步：
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        # 第三步：找到切割点
        idx = inorder.index(root_val)

        # 第四步：切割 inorder 数组，得到 inorder 数组的左，右半边
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx + 1:]

        # 第五步：切割 preorder 数组，得到 preorder 数组的左，右半边
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[1 + len(left_inorder):]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


def pre_traversal(root: TreeNode) -> List:
    vals = []

    def traversal(root: TreeNode):
        if root is None:
            return

        vals.append(root.val)
        traversal(root.left)
        traversal(root.right)

    traversal(root)
    return vals


def pre_traversal2(root: TreeNode) -> List:
    vals = []
    if root is None:
        return vals

    stack = [root]
    while stack:
        print("stack", stack)
        cur = stack.pop()
        vals.append(cur.val)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return vals


if __name__ == "__main__":
    preorders = [3, 9, 20, 15, 7]
    inorders = [9, 3, 15, 20, 7]

    root = Solution().buildTree(preorders, inorders)
    print(pre_traversal(root))
    print(pre_traversal2(root))
