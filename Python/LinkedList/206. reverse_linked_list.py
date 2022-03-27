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


class S:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


class S3:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        h = head
        stack = []
        while h:
            stack.append(h)
            h = h.next

        dummy = ListNode()
        reverse_node = dummy
        while stack:
            node = stack.pop()
            node.next = None
            dummy.next = node
            dummy = dummy.next

        return reverse_node.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().reverseList(head))
    # print(S3().reverse_linked_list(head))
