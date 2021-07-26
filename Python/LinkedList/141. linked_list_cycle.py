#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/linked-list-cycle/
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""

from utils.node import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow, fast = head, head
        count = 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            print("==count", count)
            if fast == slow:
                return True
            count += 1

        return False


if __name__ == "__main__":
    l3 = l3_1 = ListNode(3)
    l3_1.next = ListNode(2)
    l3_1 = l3_1.next
    l3_1.next = ListNode(0)
    l3_1 = l3_1.next
    l3_1.next = ListNode(-4)
    l3_1 = l3_1.next
    l3_1.next = ListNode(2)
    # l3_1 = l3_1.next
    # l3_1.next = ListNode(3)
    print(Solution().hasCycle(l3))
