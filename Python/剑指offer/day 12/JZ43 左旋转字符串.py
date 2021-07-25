#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 10/08/20

"""
题目描述：
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个
指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列
S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

"""


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0 or n <= 0:
            return s

        chars = []
        for char in s:
            move_idx = s.index(char) - n
            if move_idx < 0:
                chars.append(char)
            else:
                chars.insert(s.index(char) - n, char)

        return ''.join(chars)


class Solution2:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0 or n <= 0:
            return s

        return s[n:] + s[:n]


if __name__ == "__main__":
    print(Solution().LeftRotateString("adcXYZ", 5))
    print(Solution2().LeftRotateString("helloWORld", 5))
