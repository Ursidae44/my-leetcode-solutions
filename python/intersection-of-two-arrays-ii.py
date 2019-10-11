# https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""
Description
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
Accepted
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Preparation - find out which is smaller and sorth both lists
        if len(nums1) < len(nums2):
            smaller = sorted(nums1)
            larger = sorted(nums2)
        else:
            smaller = sorted(nums2)
            larger = sorted(nums1)

        # We will compile a result as we go
        result = []

        # We will use two pointers and process each element of both lists at most once!
        smaller_index = 0
        larger_index = 0

        # Keep processing until we've reached the end of either list
        while smaller_index < len(smaller) and larger_index < len(larger):
            # Here I'm going to name our current inspections left and right to help visualize in my head
            # The smaller is always on the left
            left = smaller[smaller_index]
            right = larger[larger_index]

            # If we have a match, add to result and advance BOTH pointers
            if left == right:
                result.append(left)
                smaller_index += 1
                larger_index += 1
            else:
                # If left is larger, move right index
                # If right is larger, move left index
                if left > right:
                    larger_index += 1
                else:
                    smaller_index += 1

        return result


class Solution_initial:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                result.append(x)
        return result
