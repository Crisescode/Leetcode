#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 17/09/20

# https://leetcode-cn.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# For example, Given Input: (2 -> 4 -> 3) + (5 -> 6-> 4), Output will be: 7 -> 0 -> 8.
# Explanation: 342 + 465 = 807.
#
from Utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        node1, node2 = [], []
        while l1:
            node1.append(l1.val)
            l1 = l1.next

        while l2:
            node2.append(l2.val)
            l2 = l2.next

        def cal_num(nums):
            num = 0
            for i in range(len(nums)):
                num += 10 ** i * nums[i]

            return num

        nums = [int(i) for i in str(cal_num(node1) + cal_num(node2))]
        print(nums)
        res = node = ListNode(0)
        for i in range(len(nums)):
            node.next = ListNode(nums[-i-1])
            node = node.next

        return res.next


if __name__ == "__main__":
    l1 = l1_1 = ListNode(2)
    l1_1.next = ListNode(3)
    l1_1 = l1_1.next
    l1_1.next = ListNode(4)
    l1_1 = l1_1.next

    l2 = l2_1 = ListNode(5)
    l2_1.next = ListNode(6)
    l2_1 = l2_1.next
    l2_1.next = ListNode(4)
    l2_1 = l2_1.next

    print(Solution().addTwoNumbers(l1, l2))
