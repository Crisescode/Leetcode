#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 08/07/20

"""
题目描述：
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、
case等关键字及条件判断语句（A?B:C）。

"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        try:
            res % n
            res += self.Sum_Solution(n - 1)
        except ZeroDivisionError:
            return 0

        return res


class Solution2:
    def Sum_Solution(self, n):
        # write code here
        res = n
        tmp = (res and self.Sum_Solution(n - 1))
        res += tmp

        return res


if __name__ == "__main__":
    print(Solution().Sum_Solution(5))
    print(Solution2().Sum_Solution(6))
