#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/unique-binary-search-trees/
# Given an integer n, return the number of structurally unique BST's (binary search trees)
# which has exactly n nodes of unique values from 1 to n
#

"""
Example 1:
 1    ...
 \
  3
  /
2

    Input: n = 3
    Output: 5
Example 2:

    Input: n = 1
    Output: 1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n: int) -> int:
        g = [0] * (n + 1)
        g[0], g[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                g[i] += g[j - 1] * g[i - j]

        print("g: ", g)
        return g[-1]


if __name__ == "__main__":
    print(Solution().numTrees(3))
