# https://leetcode.com/problems/excel-sheet-column-number/

"""
Description

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        # This problem represents a number system that is base 26
        # First we construct a conversion from letter to integer value
        number_system = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))

        # Now we start on the right hand side and work towards the left
        # Each letter will have it's lookup multipled by a power of 26
        # So first column is 26^0, then 26^1, etc
        result = 0
        power = 0
        for digit in reversed(s):
            result = result + ((26 ** power) * number_system[digit])
            power = power + 1
        return result
