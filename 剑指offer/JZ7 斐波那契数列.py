#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 07/07/20

"""
题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39

"""


# 递归法
# 时间复杂度： O(2^n)
# 空间复杂度： O(1)
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)


# 直接赋值法
# 时间复杂度： O(n)
# 空间复杂度： O(1)
class Solution2:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n

        n1, n2, n3 = 0, 1, 0
        for i in range(1, n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n3


# 优化存储
# 时间复杂度： O(n)
# 空间复杂度： O(1)
class Solution3:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n

        sum, one = 1, 0
        for i in range(1, n):
            sum = sum + one
            one = sum - one

        return sum


if __name__ == "__main__":
    print(Solution().Fibonacci(8))
    print(Solution2().Fibonacci(8))
    print(Solution3().Fibonacci(8))
