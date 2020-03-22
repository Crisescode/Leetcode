
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # left_bracket = '({['
        # right_bracket = ')}]'
        #
        # bracket_num = 0
        # for single_char in s:
        #     if single_char in left_bracket:
        #         bracket_num += 1
        #     elif single_char in right_bracket:
        #         bracket_num -= 1
        #     else:
        #         pass
        #
        # if bracket_num != 0:
        #     return False
        #
        # return True


if __name__ == "__main__":
    input_str = '(([{}]))'
    print(Solution().isValid(input_str))
