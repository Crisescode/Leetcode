#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
快速排序：
从数列中挑出一个元素，称为“基准”（pivot），重新排序数列，所有比基准值小的元素摆放在基准前面，
所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。
在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。

时间复杂度： O(nlogn)
空间复杂度： O(n)
"""

import timeit
from typing import List


class Solution:
    def quick_sort(self, l: List) -> List:
        # print(l)
        if len(l) <= 1:
            return l

        pivot = l[0]
        less_pivot = [num for num in l if num < pivot]
        greater_pivot = [num for num in l if num > pivot]

        return self.quick_sort(less_pivot) + [pivot] + self.quick_sort(greater_pivot)


if __name__ == "__main__":
    need_sort_list = [2, 4, 8, 1, 7, 10, 12, 15, 3]
    print("raw list: ", need_sort_list)
    start = timeit.default_timer()
    print("sorted list: ", Solution().quick_sort(need_sort_list))
    end = timeit.default_timer()
    elapsed = end - start
    print('{0} run time: {1} '.format(Solution().quick_sort.__qualname__, elapsed))
