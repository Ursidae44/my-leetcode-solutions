# https://leetcode.com/problems/height-checker/

"""
Description
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)



Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.


Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100
Accepted
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # We can get the correct sorting very easily
        sorted_list = sorted(heights)

        # Now we go through and compare our version against the target
        out_of_order = 0

        for index, student in enumerate(heights):
            if student != sorted_list[index]:
                out_of_order = out_of_order + 1

        return out_of_order
