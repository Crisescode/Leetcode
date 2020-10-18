#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 13/09/20

# https://leetcode-cn.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it is able to trap after raining.
#
# Example:
# Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        res = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for j in range(0, i):
                max_left = max(max_left, height[j])

            for j in range(i, len(height)):
                max_right = max(max_right, height[j])

            if min(max_left, max_right) > height[i]:
                res += min(max_left, max_right) - height[i]

        return res


# 备忘录方法，提前计算好左右最大值
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        max_left = [height[0]]
        max_right = [height[len(height) - 1]]
        res = 0

        for i in range(1, len(height)):
            left = max(height[i], max_left[i - 1])
            max_left.append(left)

        reversed_height = list(reversed(height))
        for i in range(1, len(reversed_height)):
            right = max(reversed_height[i], max_right[0])
            max_right.insert(0, right)

        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]

        return res


# 双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution3:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left, right, res = 0, len(height) - 1, 0

        max_left = height[0]
        max_right = height[len(height) - 1]

        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution2().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution3().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
