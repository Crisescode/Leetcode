#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
"""
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []
"""

from typing import List


# 方法一，暴力解法，直接超时，另寻他法了
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return []

        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in res:
                            res.append(sorted([nums[i], nums[j], nums[k]]))

        return res


class Solution2:
    def remove_duplicate_nums(self, nums: List[List[int]]) -> List[List[int]]:
        res = []
        for item in nums:
            if item not in res:
                res.append(item)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)

        print("=== nums", nums)

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return self.remove_duplicate_nums(result) if result else []

            left = i + 1
            right = len(nums) - 1
            while right > left:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    right -= 1
                    left += 1

        return self.remove_duplicate_nums(result)


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return result

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while right > left:
                # print("==== i, left, right", i, left, right, result)
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[left] == nums[left + 1]: left += 1
                    while right > left and nums[right] == nums[right - 1]: right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    # print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution2().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution3().threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]))
