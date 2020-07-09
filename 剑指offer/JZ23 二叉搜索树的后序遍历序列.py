#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 09/07/20

"""
题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

时间复杂度： O(n)
空间复杂度： O(n)
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False

        root = sequence[-1]
        for index, value in enumerate(sequence):
            if value > root:
                break

        for value in sequence[index: -1]:
            if value < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[index: -1])

        return left and right


if __name__ == "__main__":
    is_binary_tree = [1, 3, 5, 9, 12, 10, 7]
    print(Solution().VerifySquenceOfBST(is_binary_tree))