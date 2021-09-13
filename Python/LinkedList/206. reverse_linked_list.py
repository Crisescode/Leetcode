#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/reverse-linked-list/
# Reverse Linked List
# For example, Given Input: 1->2->3->4->5->NULL, Output will be: 5->4->3->2->1->NULL.
#
from Utils.timer_decorater import timer
from utils.node import ListNode


class Solution(object):
    @timer
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


if __name__ == "__main__":
    curr = head = ListNode(0)
    head.next = ListNode(1)
    head = head.next
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    head = head.next
    # print(head)
    print(curr)

    res = Solution().reverseList(curr)
    print(res)

