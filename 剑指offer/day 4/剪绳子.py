#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目描述：
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

"""


class Solution:
    def back_track(self, number):
        if number <= 4:
            return number

        ret = 0
        for i in range(1, number):
            ret = max(ret, i * self.back_track(number - i))

        return ret

    def cutRope(self, number):
        # write code here
        if number == 2: return 1
        elif number == 3: return 2

        return self.back_track(number)


# dp
class Solution2:
    def cutRope(self, number):
        f = [0]
        if number == 2:
            return 1
        if number == 3:
            return 2

        for i in range(1, 5):
            f.append(i)

        for i in range(5, number):
            for j in range(1, i):
                f[i] = max(f[i], j * f[i - j])

        return f[number]


if __name__ == "__main__":
    print(Solution().cutRope(8))
    print(Solution2().cutRope(8))
