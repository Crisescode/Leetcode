#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


if __name__ == "__main__":
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    print(Solution().findKthLargest(nums, k))
