#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum
# length of s is 1000.
#

# For example:
'''
Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:
    Input: "cbbd"
    Output: "bb
'''
from utils.timer_decorater import timer


class Solution:
    @timer
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        res = s[0]

        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j - i + 1 > max_len and self.__valid_palindromic_str(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res

    def __valid_palindromic_str(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = "abcscbmsadd"
    print(Solution().longestPalindrome(s))
