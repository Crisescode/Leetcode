#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int = None, next: "ListNode" = None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     if self:
    #         return '{0} -> {1}'.format(self.val, self.next)
