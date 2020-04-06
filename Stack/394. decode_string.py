#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/decode-string/
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only
# for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# For example:
'''
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                multi, res = 0, ""
            elif c == ']':
                cur_multi, laset_res = stack.pop()
                res = laset_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c

        return res


if __name__ == "__main__":
    # str_input = "3[a2[c]]"
    str_input = '2[abc]3[cd]ef'
    print(Solution().decodeString(str_input))
