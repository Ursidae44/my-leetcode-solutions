# https://leetcode.com/problems/jewels-and-stones/

"""
Description
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # First of all, short variable names are hard to keep track of
        jewels = J
        stones_on_hand = S

        # We can use a list comprehension to sort out what we have that are stones
        jewels_on_hand = [x for x in stones_on_hand if x in jewels]

        # And finally we want to know how many jewels we have
        return len(jewels_on_hand)
