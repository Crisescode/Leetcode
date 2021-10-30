#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/count-complete-tree-nodes/
# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete
# binary tree, and all nodes in the last level are as far left as possible. It can have between 1
# and 2h nodes inclusive at the last level h.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
Example:
    Input:
                    1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
    Input: root = [1, 2, 3, 4, 5, 6, 7]
    Output: 7
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> (int, List):
        result = 0
        # l_results = []

        if not root:
            return result

        from collections import deque
        queue = deque([root])
        while queue:
            # l_result = []
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                # l_result.append(cur.val)
                result += 1

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            # l_results.append(l_result)

        return result


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = root.left
        right = root.right

        left_height, right_height = 0, 0
        while left:
            left = left.left
            left_height += 1

        while right:
            right = right.right
            right_height += 1

        if left_height == right_height:
            return (2 << left_height) - 1

        left_h = self.countNodes(root.left)
        right_h = self.countNodes(root.right)
        return left_h + right_h + 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    # print(Solution().countNodes(root))
    print(Solution2().countNodes(root))
