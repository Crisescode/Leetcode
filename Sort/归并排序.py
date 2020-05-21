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
    def merge_sort(self, l: List) -> List:
        if len(l) <= 1:
            return l

        mid = len(l) // 2
        l_left = l[:mid]
        l_right = l[mid:]
        l_left = self.merge_sort(l_left)
        l_right = self.merge_sort(l_right)

        return self.merge(l_left, l_right)

    def merge(self, left, right):
        # l_index, r_index = 0, 0
        # result = []
        # while l_index < len(left) and r_index < len(right):
        #     if left[l_index] < right[r_index]:
        #         result.append(left[l_index])
        #         l_index += 1
        #     else:
        #         result.append(right[r_index])
        #         r_index += 1
        #
        # result += left[l_index:]
        # result += right[r_index:]
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        if left or right:
            result += left or right

        return result


if __name__ == "__main__":
    need_sort_list = [2, 4, 8, 1, 7, 10, 12, 15, 3]
    print("raw list: ", need_sort_list)
    start = timeit.default_timer()
    print("sorted list: ", Solution().merge_sort(need_sort_list))
    end = timeit.default_timer()
    elapsed = end - start
    print('{0} run time: {1} '.format(Solution().merge_sort.__qualname__, elapsed))
