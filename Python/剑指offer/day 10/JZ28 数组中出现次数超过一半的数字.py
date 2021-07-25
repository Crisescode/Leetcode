#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 27/07/20

"""
题目描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0

        length = len(numbers)
        hash_map = {}
        for num in numbers:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        nums = [num for num in hash_map.keys() if hash_map[num] > length / 2]
        return nums[0] if nums else 0


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().MoreThanHalfNum_Solution(numbers))
