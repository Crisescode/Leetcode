#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# 输入整数数组arr, 找出其中最小的k个数。
# 例如, 给定输入为：[3， 2， 1], k = 2
# 输出为：[1, 2] 或 [2, 1]
#
# 限制：0 <= k <= len(arr) <=10000, 0 <= arr[i] <= 10000
#

from typing import  List


class Solution:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        less_pivot = [num for num in arr[1:] if num <= pivot]
        greater_pivot = [num for num in arr[1:] if num > pivot]

        return self.quick_sort(less_pivot) + [pivot] + self.quick_sort(greater_pivot)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= k:
            return arr

        sorted_arr = self.quick_sort(arr)
        return sorted_arr[:k]


class Solution2:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= k:
            return arr

        return sorted(arr)[:k]


if __name__ == "__main__":
    # arr_input, k = [4, 15, 10, 6, 3, 62, 71, 8], 4
    arr_input, k = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8
    print(Solution().getLeastNumbers(arr_input, k))
    print(Solution2().getLeastNumbers(arr_input, k))

