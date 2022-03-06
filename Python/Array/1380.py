from typing import List, Any


class Solution:
    def find_max(self, nums: Any, is_max: bool = True) -> (int, int):
        res = nums[0]
        idx_res = 0
        if is_max:
            for idx, num in enumerate(nums[1:]):
                if num > res:
                    res = num
                    idx_res = idx + 1
        else:
            for idx, num in enumerate(nums[1:]):
                if num < res:
                    res = num
                    idx_res = idx + 1

        return res, idx_res

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_map = {}
        for idx, val in enumerate(matrix):
            v, y = self.find_max(val, is_max=False)
            row_map[v] = (idx, y)
            print(f"min value: index: {(idx, y)}, val: {v}")

        print(list(zip(*matrix)))
        col_map = {}
        for idx, val in enumerate(list(zip(*matrix))):
            v, y = self.find_max(val, is_max=True)
            col_map[v] = (y, idx)
            print(f"max value: index: {(idx, y)}, val: {v}")

        res = []
        for key, val in row_map.items():
            if key in col_map and row_map[key] == col_map[key]:
                res.append(key)

        return res


class Solution2:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(nums) for nums in matrix]
        col_max = [max(nums) for nums in zip(*matrix)]

        return list(set(row_min) & set(col_max))


if __name__ == "__main__":
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(Solution().luckyNumbers(matrix))
    print(Solution2().luckyNumbers(matrix))
