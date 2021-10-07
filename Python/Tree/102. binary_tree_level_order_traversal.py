#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Given a binary tree, return the level order traversal of its nodes' values
# (ie, from left to right, level by level).

"""
Example:
    Input:
                3
               / \
              9   20
                 / \
                15  7
    Input: root = [3, 9, 20, null, null. 15, 7]
    Output:
           [[3], [9, 20], [15, 7]]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            q_len = len(que)
            result = []
            for _ in range(q_len):
                cur = que.popleft()
                result.append(cur.val)

                if cur.left:
                    que.append(cur.left)

                if cur.right:
                    que.append(cur.right)

            results.append(result)

        return results[::-1]


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(Solution().levelOrderTraversal(tree))
