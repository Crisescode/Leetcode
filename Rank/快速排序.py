#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
归并排序：
归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

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
