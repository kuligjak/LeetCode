# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        mapping = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        s = list(s)
        max_index = len(s) - 1
        index = 0
        roman_numbers = []

        while index <= max_index:
            current_roman_number = s[index]
            if index < max_index:
                next_roman_number = s[index + 1]
            else:
                next_roman_number = ''

            tl = current_roman_number + next_roman_number

            if tl in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                roman_numbers.append(tl)
                index = index + 2
            else:
                roman_numbers.append(current_roman_number)
                index = index + 1

        for number in roman_numbers:
            result = result + mapping[number]

        return result