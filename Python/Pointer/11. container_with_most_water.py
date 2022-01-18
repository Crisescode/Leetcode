#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/container-with-most-water/
# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
"""
Example 1:

    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, (j - i) * height[i])
                i += 1
            else:
                res = max(res, (j - i) * height[j])
                j -= 1

        return res


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
