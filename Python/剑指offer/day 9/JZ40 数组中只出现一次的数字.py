#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 25/07/20

"""
题目描述：
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array is None:
            return

        hash_map = {}
        for num in array:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        res = [num for num in hash_map.keys() if hash_map[num] == 1]
        return res


if __name__ == "__main__":
    print(Solution().FindNumsAppearOnce([2, 3, 1, 5, 1, 3, 6, 11, 6, 0, 11, 5]))
