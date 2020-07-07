#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 07/07/20

"""
题目描述：
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述：
输入一个字符串,包括数字字母符号,可以为空
输出描述：
如果是合法的数值表达则返回该数字，否则返回0

示例：
输入：
+2147483647
1a33

输出：
2147483647
0
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0

        str2num = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "+": 1, "-": -1
        }

        sum = 0
        sign = 1
        for c in s:
            if c in str2num:
                if c == "+":
                    sign = str2num["+"]
                    continue
                if c == "-":
                    sign = str2num["-"]
                    continue
                sum = sum * 10 + str2num[c]
            else:
                sum = 0
                break

        return sum * sign


if __name__ == "__main__":
    s = "-98210"
    print(Solution().StrToInt(s))
