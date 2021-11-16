#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/perfect-rectangle/
# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned
# rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of
# it is (ai, bi).
#
# Return true if all the rectangles together form an exact cover of a rectangular region.
#
#
"""
Example:
    Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
    Output: true
    Explanation: All 5 rectangles together form an exact cover of a rectangular region.
"""

from typing import List
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)

        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]
            area += (a - x) * (b - y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[(minX, maxY)] != 1 or cnt[(maxX, maxY)] != 1 or cnt[(maxX, minY)] != 1:
            return False

        del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        return all(c == 2 or c == 4 for c in cnt.values())


if __name__ == "__main__":
    rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print(Solution().isRectangleCover(rectangles=rectangles))
