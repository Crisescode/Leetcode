#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/rotate-string/
# Given two strings s and goal, return true if and only if s can become
# goal after some number of shifts on s.
#
"""
Example 1:

    Input: s = "abcde", goal = "cdeab"
    Output: true

Example 2:

    Input: s = "abcde", goal = "abced"
    Output: false
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for idx, c in enumerate(s):
            rotata_s = s[idx:] + s[:idx]
            if rotata_s == goal:
                return True

        return False


if __name__ == "__main__":
    print(Solution().rotateString("abcde", "abced"))
