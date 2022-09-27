#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# For example, Given Input: 1->2-3->4, Output will be: 2->1->4->3.
#
from Utils.timer_decorater import timer
from utils import ListNode


class Solution:
    @timer
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy_head = ListNode()
        pre = dummy_head
        p = head

        while p and p.next:
            tmp = p.next

            pre.next = tmp
            p.next = tmp.next
            tmp.next = p

            pre = p
            p = p.next

        return dummy_head.next


def travel_listed_list(head: ListNode):
    vals = []

    if head is None:
        return vals

    while head:
        vals.append(head.val)
        head = head.next

    return vals


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        while cur.next is not None and cur.next.next is not None:
            tmp1 = cur.next
            tmp2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = tmp1
            tmp1.next = tmp2

            cur = cur.next.next

        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    # print(travel_listed_list(Solution().swapPairs(head)))
    print(travel_listed_list(Solution2().swapPairs(head)))
