class Solution:
    def swap_and_find_num(self, num):
        if num <= 10:
            return num

        nums = [i for i in str(num)]
        def find_max_index(nums):
            max_num = 0
            index = 0
            for i, n in enumerate(nums):
                if int(n) > max_num:
                    max_num = int(n)
                    index = i

            return index

        for i in range(len(nums)):
            max_num_index = find_max_index(nums[i:]) + i
            if i == max_num_index:
                continue
            else:
                nums[i], nums[max_num_index] = nums[max_num_index], nums[i]
                break

        return int(''.join(nums))


if __name__ == "__main__":
    print(Solution().swap_and_find_num(1993))
