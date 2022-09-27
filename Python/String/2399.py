# coding: utf-8

from typing import List
from collections import defaultdict


class Solution:
    def checkDistance(self, s: str, distance: List[int]) -> bool:
        char_idx = defaultdict(list)
        for idx, c in enumerate(s):
            char_idx[c].append(idx)

        for c, idxs in char_idx.items():
            dis = ord(c) - ord('a')
            if distance[dis] != idxs[1] - idxs[0] - 1:
                return False
        return True


if __name__ == "__main__":
    s = "abcabc"
    distance = [0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    res = Solution().checkDistance(s, distance)
    print(res)
