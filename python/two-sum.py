# https://leetcode.com/problems/two-sum/

"""
Description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a dictionary storing the index of values as we go
        complements = {}

        for index, value in enumerate(nums):
            # Calculate the number we would need for a solution
            complement = target - value
            # print('comp', comp, complements)
            # If we know the index of that value, we have our solution
            if complement in complements:
                return [complements[complement], index]
            else:
                # If we don't know that index yet, mark down the index for our current number in case we need it later
                complements[value] = index

    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for inner_index, inner_value in enumerate(nums):
                # print('index: {} value: {} inner_index: {} inner_value: {}'.format(index, value, inner_index, inner_value))
                if (value + inner_value == target) and index != inner_index:
                    return [index, inner_index]
