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
        if len(matrix) == 1:
            return matrix[0][0]

        row_min = 0
        row_max = len(matrix)
        col_min = 0
        col_max = len(matrix[0])

        # 向右
        res = [matrix[0][j] for j in range(col_max)]
        res.extend([matrix[i][col_max - 1] for i in range(row_min + 1, row_max)])
        res.extend([matrix[row_max - 1][j] for j in range()])
        print(res)


if __name__ == "__main__":
    num = 1
    matrix = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = num
            num += 1
    print(matrix)

    print(Solution().printMatrix(matrix))
