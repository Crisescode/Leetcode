#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Time:  O(n)
# Space: O(1)
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
from utils.timer_decorater import timer


class Solution:
    @timer
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        res, i = 0, 0

        for j in range(len(s)):
            # move start flag
            if s[j] in st:
                i = max(i, st[s[j]])

            res = max(res, j - i + 1)
            st[s[j]] = j + 1

        return res


if __name__ == '__main__':
    solu = Solution()
    reslut = solu.lengthOfLongestSubstring('abcabcbb')
    assert reslut == 3
    print(reslut)
