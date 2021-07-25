#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 15/07/20

"""
题目描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        res = []
        while top < bottom and left < right:
            # 向右
            res.extend([matrix[top][c] for c in range(left, right)])
            # 向下
            res.extend([matrix[r][right - 1] for r in range(top + 1, bottom)])
            # 向左
            if bottom - top > 1:
                res.extend([matrix[bottom - 1][c] for c in range(right - 2, left, -1)])
            # 向上
            if right - left > 1:
                res.extend([matrix[r][left] for r in range(bottom - 1, top, -1)])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res


if __name__ == "__main__":
    num = 1
    matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = num
            num += 1

    print(Solution().printMatrix(matrix))
    print(Solution().printMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
