#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 08/07/20

"""
题目描述：
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0

        if n < 0:
            n = n & 0b11111111111111111111111111111111

        while n != 0:
            count += 1
            n = n & (n - 1)

        return count


if __name__ == "__main__":
    print(Solution().NumberOf1(-11))
