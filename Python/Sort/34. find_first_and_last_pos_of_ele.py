
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        for idx, num in enumerate(nums):
            if num == target:
                res.append(idx)

        if len(res) > 1:
            return [res[0], res[-1]]

        if len(res) == 1:
            return [res[0], res[0]]

        if len(res) == 0:
            return [-1, -1]


if __name__ == "__main__":
    print(Solution().searchRange([1, 2, 2, 3, 4, 5, 5, 5, 6, 8, 10, 10, 20, 21], 6))