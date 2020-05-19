#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
冒泡排序：
1. 比较相邻的两个元素，如果前一个比后一个大，进行交换；
2. 对每一对相邻的元素进行step 1操作，第一轮完成，数组中的最后一个元素会是最大的元素；
3. 对接下来的每一轮进行同样的操作，将最大的数冒泡到最后的位置，直到不需要再交换为止。

时间复杂度： O(n^2)
空间复杂度： O(1)
"""

from utils.timer_decorater import timer
from typing import List


class Solution:
    @timer
    def bubble_sort(self, l: List) -> List:
        if len(l) <= 1:
            return l

        for index in range(len(l)):
            for j in range(1, len(l) - index):
                if l[j - 1] > l[j]:
                    l[j - 1], l[j] = l[j], l[j - 1]
        return l


# 优化
class Solution2:
    @timer
    def bubble_sort(self, l: List) -> List:
        if len(l) <= 1:
            return l

        for index in range(len(l)):
            flag = True
            for j in range(1, len(l) - index):
                if l[j - 1] > l[j]:
                    l[j - 1], l[j] = l[j], l[j - 1]
                    flag = False

            if flag:
                return l

        return l


if __name__ == "__main__":
    need_sort_list = [2, 4, 8, 1, 7, 10, 12, 15, 3]
    print(Solution().bubble_sort(need_sort_list))
    print(Solution2().bubble_sort(need_sort_list))
