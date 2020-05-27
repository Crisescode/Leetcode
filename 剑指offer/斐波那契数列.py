#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39

时间复杂度： O(n)
空间复杂度： O(n)
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)


class Solution2:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        n1, n2, n3 = 0, 1, 0
        for i in range(3, n + 1):
            # print(i)
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n3


if __name__ == "__main__":
    print(Solution().Fibonacci(8))
    print(Solution2().Fibonacci(8))
