#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 12/07/20

"""
题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

"""


class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number

        res, counter = 1, 0
        for i in range(1, number + 1):
            res = res + counter
            counter = res - counter

        return res


if __name__ == "__main__":
    print(Solution().rectCover(4))
