# https://leetcode.com/problems/reverse-string 

"""
Description:
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # There is a standard library way to do this already
        # s.reverse()

        # Manual way: 
        # Rebuild the string 
        # Move the last element to the new spot as you move from the start of the list onward
        for index in range(len(s)):
            s.insert(index, s.pop())

        # Also, why are we mutating function parameters?
