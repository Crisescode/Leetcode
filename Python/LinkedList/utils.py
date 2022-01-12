#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next_=None):
        self.val = x
        self.next = None
        self.next_ = next_

    def __repr__(self):
        if self:
            return '{0} -> {1}'.format(self.val, self.next)
