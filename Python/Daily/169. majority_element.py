#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element
# is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# For example, Given Input = [3, 2, 3], output will be 3. Given Input = [2, 2, 1, 2, 1, 1, 2], Output will be 2.
#
from Utils.timer_decorater import timer


class Solution(object):
    @timer
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None

        num_count = {}
        for i in nums:
            if i in num_count.keys():
                num_count[i] += 1
            else:
                num_count[i] = 1

        res = []
        for k, v in num_count.items():
            if v > len(nums) / 2:
                res.append(k)
            else:
                pass

        return res if res else None


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 3, 2, 2, 3, 3, 3, 3, 3, 3]
    print(Solution().majorityElement(nums))
