
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        data = []

        for sc in s:
            if sc in bracket_dict:
                data.append(sc)
                continue
            if data and sc == bracket_dict[data[-1]]:
                data.pop()
            else:
                return False

        return True if not data else False


if __name__ == "__main__":
    input_str = '(([{}]))'
    print(Solution().isValid(input_str))
