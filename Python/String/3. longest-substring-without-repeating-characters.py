#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Time:  O(n)
# Space: O(1)
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
from Utils.timer_decorater import timer


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


class Solution2:
    @timer
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        lookup = set()
        cur_len, max_len = 0, 0

        for idx in range(len(s)):
            cur_len += 1
            while s[idx] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1

            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[idx])

        return max_len


if __name__ == '__main__':
    solu = Solution()
    reslut = solu.lengthOfLongestSubstring('abcabcbb')
    print(reslut)

    # solu2 = Solution2()
    # reslut2 = solu2.lengthOfLongestSubstring('dvdf')
    # print(reslut2)
