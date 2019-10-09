# https://leetcode.com/problems/single-number/

"""
Description
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # We total up the number of occurrences of each integer as we go
        count_hash = {}
        for number in nums:
            count_hash[number] = count_hash.get(number, 0) + 1

        # And then we return the integer that had only one occurence
        return [x for x in count_hash if count_hash[x] == 1][0]
