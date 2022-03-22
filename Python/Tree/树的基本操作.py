#! /usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class TreeNodeOpr:
    def pre_order_traversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res

    def in_order_traversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
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

    def post_order_traversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()

        return res[::-1]

    def level_order_traversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        from collections import deque
        q = deque()
        q.append(root)
        # curr = root
        # q = [curr]
        while q:
            curr = q.popleft()
            res.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return res

    def level_order_traversal_2(self, root: TreeNode) -> List:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            res.append([node.val for node in stack])
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]

        return res


if __name__ == "__main__":
    """
             4
           /  \
          2    7
         / \  / \
        1   3 6  9
    """
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(7)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)
    tree1.right.left = TreeNode(6)
    tree1.right.right = TreeNode(9)

    print("----------- 迭代方法 -------------")
    print("前序遍历：", TreeNodeOpr().pre_order_traversal(tree1))
    print("中序遍历：", TreeNodeOpr().in_order_traversal(tree1))
    print("后序遍历：", TreeNodeOpr().post_order_traversal(tree1))

    print("----------- 层次遍历 -------------")
    print(TreeNodeOpr().level_order_traversal(tree1))
    print("----------- 层次遍历 2 -------------")
    print(TreeNodeOpr().level_order_traversal_2(tree1))
