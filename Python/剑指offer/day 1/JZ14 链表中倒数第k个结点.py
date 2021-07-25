#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 06/07/20

"""
题目描述：
输入一个链表，输出该链表中倒数第k个结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ReSolution:
    def FindKthToTail(self, head, k):
        if head is None:
            return

        fast = slow = head
        for i in range(k):
            fast = fast.next if fast else None

        if fast is None:
            return slow.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


class Solution:
    # 时间复杂度： O(n)
    # 空间复杂度： O(n)
    def FindKthToTail(self, head, k):
        # write code here
        res = []

        while head is not None:
            res.insert(0, head.val)
            head = head.next

        print("res:", res)
        if len(res) < k or k < 1:
            return

        return res[k-1]

    def travel_listNode(self, listNode):
        while listNode:
            print(listNode.val, end=" ")
            listNode = listNode.next


class Solution2:
    # 时间复杂度： O(n)
    # 空间复杂度： O(1)
    def FindKthToTail(self, head, k):
        # write code here
        if k < 0 or head is None:
            return

        slow, fast = head, head
        count = 0
        while fast.next is not None:
            fast = fast.next
            if count >= k - 1:
                slow = slow.next
            count += 1

        if count >= k - 1:
            return slow.val

        return None


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
    print(Solution().FindKthToTail(curr, 3))
    print(Solution2().FindKthToTail(curr, 3))
    print(Solution().travel_listNode(ReSolution().FindKthToTail(curr, 3)))
