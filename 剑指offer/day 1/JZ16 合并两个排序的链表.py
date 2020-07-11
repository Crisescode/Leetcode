#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Crise
# date: 06/07/20

"""
题目描述：
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        if pHead1.val < pHead2.val:
            sorted_list = pHead1
            sorted_list.next = self.Merge(pHead1.next, pHead2)
        else:
            sorted_list = pHead2
            sorted_list.next = self.Merge(pHead1, pHead2.next)

        return sorted_list

    def travel_list(self, node):
        while node is not None:
            print(node.val, end=" ")
            node = node.next


class Solution2:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        node = sorted_node = ListNode(0)

        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
            node = node.next

        if pHead1 or pHead2:
            node.next = pHead1 or pHead2

        return sorted_node.next

    def travel_list(self, node):
        while node is not None:
            print(node.val, end=" ")
            node = node.next


if __name__ == "__main__":
    node_1 = ListNode(0)
    node_1.next = ListNode(4)
    node_1.next.next = ListNode(10)
    node_2 = ListNode(2)
    node_2.next = ListNode(3)
    node_2.next.next = ListNode(12)
    solu_1 = Solution()
    print(solu_1.travel_list(solu_1.Merge(node_1, node_2)))
    solu_2 = Solution2()
    # print(solu_2.travel_list(solu_2.Merge(node_1, node_2)))

