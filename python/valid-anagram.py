# https://leetcode.com/problems/valid-anagram/

"""
Description
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Python has a built in method to sort things
        # If sort both strings alphabetically they should be equal if they are anagrams
        return sorted(s) == sorted(t)


class SolutionManual:
    def isAnagram(self, s: str, t: str) -> bool:
        # For performance reasons it is best to eliminate edge cases early
        if len(s) != len(t):
            return False

        # We'll convert our strings to list to work with one character at a time
        # As well as letting us use the remove() method
        list_s = list(s)
        list_t = list(t)

        # Now we check by removing each character from the second string
        # If we can't find the character, we immediately stop because it is not an anagram
        for character in list_s:
            try:
                list_t.remove(character)
            except ValueError:
                return False

        # If we get this far then we have an anagram
        return True
