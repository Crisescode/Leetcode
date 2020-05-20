#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
选择排序：
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
    def selection_sort(self, l: List) -> List:
        if len(l) <= 1:
            return l

        for index in range(len(l)):
            min_index = index
            for j in range(index + 1, len(l)):
                if l[j] < l[min_index]:
                    min_index = j
                    l[index], l[min_index] = l[min_index], l[index]

        return l


if __name__ == "__main__":
    need_sort_list = [2, 4, 8, 1, 7, 10, 12, 15, 3]
    print(Solution().selection_sort(need_sort_list))
