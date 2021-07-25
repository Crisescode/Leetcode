import sys


# def count_fun(string_input):
#     count = 0
#     for char in string_input:
#         if char == "a":
#             count += 1
#     return count
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     string_input = sys.stdin.readline().strip()
#
#     print(count_fun(string_input))


# def find_char(str_inp):
#     char_num = {}
#     for char in str_inp:
#         if char in char_num:
#             char_num[char] += 1
#         else:
#             char_num[char] = 1
#
#     max_num = max(char_num.values())
#
#     return list(sorted(c for c, v in char_num.items() if v == max_num))[0]


# def sort_str(str_inp):
#     char_num = {}
#     for char in str_inp:
#         if char in char_num:
#             char_num[char] += 1
#         else:
#             char_num[char] = 1
#
#     sorted_chars = sorted(char_num.items(), key=lambda x: (-x[1], x[0]))
#
#     sorted_str = ""
#     for item in sorted_chars:
#         sorted_str += item[0] * item[1]
#
#     return sorted_str


def find_res(nums):
    pass


if __name__ == "__main__":
    nums_inp = []
    for i in range(5):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        nums_inp.append(values)
    print(nums_inp)

    find_res(nums_inp)
