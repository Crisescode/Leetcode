#! /usr/bin/env python
# -*- coding: utf-8 -*-


# https://leetcode-cn.com/problems/merge-two-binary-trees/
# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise,
# the NOT null node will be used as the node of new tree.
#
"""
Example:
    Input:
              Tree 1                 Tree2
                 1                     2
               / \                    / \
             3    2                  1   3
           /                         \    \
         5                            4    7
    Output:
    Merged tree:
                          3
                         / \
                       4    5
                      / \    \
                    5    4    7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)

        setattr(self, "_root", root)

        # return root

    def preOrder(self):
        if self._root == None:
            return

        print(self._root.val, end=' ')
        self.preOrder(self._root.left)
        self.preOrder(self._root.right)


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    print(tree1.left.left.val)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)
    print(tree2.left.right.val)

    Solution().mergeTrees(tree1, tree2)
    Solution().preOrder()

