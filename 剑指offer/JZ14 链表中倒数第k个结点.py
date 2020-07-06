#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 06/07/20

"""
题目描述：
输入一个链表，输出该链表中倒数第k个结点。

时间复杂度： O(n)
空间复杂度： O(n)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        count = 0
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        while prev:
            count += 1
            if count == k:
                prev = prev.next
                return prev.val

        return None

    def travel_listNode(self, listNode):
        while listNode:
            print(listNode.val, end=" ")
            listNode = listNode.next


if __name__ == "__main__":
    curr = head = ListNode(0)
    head.next = ListNode(1)
    head = head.next
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    head = head.next
    head.next = ListNode(4) 

    print(Solution().travel_listNode(curr))
    print(Solution().FindKthToTail(curr, 2))
