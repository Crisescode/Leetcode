#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 25/07/20

"""
题目描述：
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if num is None or size <= 0:
            return []

        max_list = []
        for i in range(len(num) - size + 1):
            range_ = num[i: i+size]
            max_list.append(max(range_))
        return max_list


if __name__ == "__main__":
    print(Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 2))
