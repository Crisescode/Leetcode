#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 27/07/20

"""
题目描述：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None or k <= 0:
            return

        return self.quick_sort(tinput)[:k]

    def quick_sort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[0]
        less_pivot = [num for num in array if num < pivot]
        more_pivot = [num for num in array if num > pivot]

        return self.quick_sort(less_pivot) + [pivot] + self.quick_sort(more_pivot)


if __name__ == "__main__":
    array = [4, 5, 1, 6, 2, 7, 3, 8]
    print(Solution().GetLeastNumbers_Solution(array, 4))
