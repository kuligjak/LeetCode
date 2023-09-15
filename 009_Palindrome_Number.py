# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        lower = -2**31
        upper = (2**31)-1
        if (lower <= x <= upper) and (str(x) == str(x)[::-1]):
            return True
        else:
            return False