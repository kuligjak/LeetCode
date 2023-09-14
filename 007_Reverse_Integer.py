# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        lower = -2 ** 31
        upper = (2 ** 31) - 1
        if x < 0:
            x = int('-' + str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])

        if x >= lower and x <= upper:
            return x
        else:
            return 0
