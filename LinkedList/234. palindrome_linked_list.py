#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.
# For example, Given Input: 1->2->3, Output will be: False.
# Given Input: 1->2->3->3->2->1, Output will be: True.
#
from linked_utils.node import ListNode
from utils.timer_decorater import timer


class Solution(object):
    # Time: o(n)
    # Space: o(n)
    @timer
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        data = []
        while head:
            data.append(head.val)
            head = head.next
        # flag = True
        # for i in range(len(data) // 2):
        #     if data[i] != data[len(data)-i-1]:
        #         flag = False

        # return flag
        return data == data[::-1]


if __name__ == '__main__':
    l3 = l3_1 = ListNode(0)
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(3)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(0)

    print(Solution().isPalindrome(l3))

