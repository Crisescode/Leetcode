#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/reverse-linked-list/
# Reverse Linked List
# For example, Given Input: 1->2->3->4->5->NULL, Output will be: 5->4->3->2->1->NULL.
#
from Utils.timer_decorater import timer
from utils import ListNode


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
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    print(Solution().reverseList(head))
