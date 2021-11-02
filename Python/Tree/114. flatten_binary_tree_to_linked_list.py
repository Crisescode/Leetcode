#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
#
"""
For example, given the following tree:
                 1
               / \
             2    5
           / \    \
          3  4    6
The flattened tree should look like:
1 -> 2 -> 3 -> 4 -> 5 -> 6
"""

from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def flatten(self, root: TreeNode) -> Union[ListNode, None]:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        vals, stack = [], [root]
        while stack:
            cur = stack.pop()
            vals.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        cur_node = head = ListNode(0)
        while vals:
            cur_val = vals.pop(0)
            cur = ListNode(cur_val)
            head.next = cur
            head = head.next

        return cur_node.next


def traversal(head: ListNode) -> List[int]:
    vals = []
    if head is None:
        return vals

    while head is not None:
        vals.append(head.val)
        head = head.next

    return vals


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(6)

    print(traversal(Solution().flatten(tree)))
