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
from Utils.timer_decorater import timer


# 暴力解法：找出长度大于等于2的字串，然后判断其是否为回文子串
class Solution:
    @timer
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        res = s[0]

        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j - i + 1 > max_len and self.__valid_palindromic_str2(s, i, j):
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

    def __valid_palindromic_str2(self, s, left, right):
        sub_str = s[left:right]
        print("sub str: ", sub_str)
        if sub_str == sub_str[::-1]:
            return True


# 中心扩散法：依次遍历字符串中每个字符，然后记录其左右字符，
class Solution2:
    @timer
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        length = len(s)
        left, right, maxLen, maxStart = 0, 0, 0, 0
        lens = 1

        for i in range(length):
            left = i - 1
            right = i + 1

            while left >= 0 and s[left] == s[i]:
                left -= 1
                lens += 1
            while right < length and s[right] == s[i]:
                right += 1
                lens += 1
            while left >= 0 and right < length and s[left] == s[right]:
                lens = lens + 2
                left -= 1
                right += 1

            if lens > maxLen:
                maxLen = lens
                maxStart = left

            lens = 1

        return s[maxStart + 1:maxStart + maxLen + 1]


if __name__ == "__main__":
    s = "acmaaaamcb"
    print(Solution().longestPalindrome(s))
    print(Solution2().longestPalindrome(s))
