# https://leetcode.com/problems/move-zeroes/submissions/

"""
Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Not sure why we're mutating a parameter but lets go!

        # We keep track of where we are in the list as we are modifying it in place
        # We keep track of how many elements we've processed so we know when to stop
        index = 0
        processed = 0

        # Go until we have looked at every element
        while (processed < len(nums)):
            element = nums[index]

            if element == 0:
                # We found a zero. Move it to the end
                # Since the next number is going to shift down into this index, we don't move our index forward
                nums.append(element)
                nums.pop(index)
            else:
                # Not a zero, so just move to the next number
                index += 1

            # Either way we've looked at a new number
            processed += 1
            # print("length", len(nums), "index", index, "processed", processed)
