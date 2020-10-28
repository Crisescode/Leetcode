#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 28/10/20

# https://leetcode-cn.com/problems/unique-number-of-occurrences/
# Given an array of integers arr, write a function that returns true if and only
# if the number of occurrences of each value in the array is unique.
#
# Example:
# Input: arr = [1, 2, 2, 1, 1, 3]
# Output: true
#
# Input: arr = [1,2]
# Output: false
#
from Utils.timer_decorater import timer
from typing import List


@timer
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return True

        nums = {}
        for n in arr:
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1

        counts = list(nums.values())
        return len(counts) == len(set(counts))


if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    arr2 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(Solution().uniqueOccurrences(arr2))

