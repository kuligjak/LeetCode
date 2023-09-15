# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        mapping = {
            1: 'I', 4: 'IV',
            5: 'V', 9: 'IX',
            10: 'X', 40: 'XL',
            50: 'L', 90: 'XC',
            100: 'C', 400: 'CD',
            500: 'D', 900: 'CM',
            1000: 'M' }

        integers = list(mapping.keys())[::-1]

        while num > 0:
            for i in integers:
                if i <= num:
                    result = result + mapping[i]
                    num = num - i
                    break

        return result