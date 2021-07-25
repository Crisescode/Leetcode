#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 06/07/20

"""
题目描述：
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

时间复杂度： O(n)
空间复杂度： O(n)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next

        return res

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
    print(Solution().printListFromTailToHead(curr))
