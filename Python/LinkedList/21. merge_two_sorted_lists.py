#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# For example, Given Input: 1->2->4, 1->3->4, Output will be: 1->1->2->3->4->4.
#
from Utils.timer_decorater import timer
from utils import ListNode


class Solution(object):
    @timer
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l2 or l1

        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2

        return dummy.next


class Solution2(object):
    @timer
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        node = sorted_node = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 or l2:
            node.next = l1 or l2

        return sorted_node.next


if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode(2)
    l2.next = ListNode(3)
    print(l1)
    print(l2)
    print(Solution().mergeTwoLists(l1, l2))
    l3 = l3_1 = ListNode(0)
    l3_1.next = ListNode(1)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    l4 = l4_1 = ListNode(2)
    l4_1.next = ListNode(3)
    l4_1 = l4_1.next
    l4_1.next = ListNode(4)
    print(l3_1)
    print(l3)
    print(l4_1)
    print(l4)

    print(Solution2().mergeTwoLists(l3, l4))
