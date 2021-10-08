#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
"""
For example, this binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric:
    Symmetric tree:
                 1
               / \
             2    2
           / \   / \
          3  4  4  3
    But the following [1, 2, 2, null, 3, null, 3] is not:

                 1
               / \
             2    2
             \     \
              3     3
"""
from Utils.timer_decorater import timer


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用栈迭代法
class Solution:
    @timer
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = []
        stack.append((root, root))

        while stack:
            # 这里使用 pop(0) 左边或者使用 pop() 右边，都是可以的
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


# 使用队列迭代法
class Solution2:
    @timer
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        from collections import deque
        queue = deque()
        queue.append((root, root))

        while queue:
            # 这里使用 popleft() 左边或者使用 pop() 右边，都是可以的
            left, right = queue.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


# 递归法
class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        outs = self.compare(left.left, right.right)
        ins = self.compare(left.right, right.left)

        return outs and ins


def test_queue():
    import collections
    queue = collections.deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    print(queue.popleft())
    print(queue)
    print(queue.pop())
    print(queue)

    m = [2, 3, 4]
    print(m.pop(0))
    print(m)


if __name__ == "__main__":
    test_queue()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(3)

    print(Solution().isSymmetric(tree))
    print(Solution2().isSymmetric(tree))
