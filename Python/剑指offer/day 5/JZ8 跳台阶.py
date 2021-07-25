#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 12/07/20

"""
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number

        res, counter = 1, 0
        for i in range(1, number + 1):
            res = res + counter
            counter = res - counter

        return res


if __name__ == "__main__":
    print(Solution().jumpFloor(3))
