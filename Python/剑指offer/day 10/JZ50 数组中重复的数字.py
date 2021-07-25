#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 27/07/20

"""
题目描述：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) == 0:
            return False, 0
        stack = []
        for num in numbers:
            if num > len(numbers) - 1:
                return False, 0
            if num not in stack:
                stack.append(num)
            else:
               duplication.append(num)
               return True, duplication[0]

        return False


if __name__ == "__main__":
    # numbers = [2, 3, 1, 0, 2, 5, 3]
    numbers = [2, 1, 3, 1, 4]
    print(Solution().duplicate(numbers, []))
