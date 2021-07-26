#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_num_frequency_map = Counter(nums)
        return [item[0] for item in sorted_num_frequency_map.most_common(k)]


if __name__ == "__main__":
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [3, 0, 0, 1]
    k = 1
    print(Solution().topKFrequent(nums, k))
