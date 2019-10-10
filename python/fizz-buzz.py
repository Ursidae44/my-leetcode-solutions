# https://leetcode.com/problems/fizz-buzz/

"""
Description
Share
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # The output is expected to be a list of strings
        output = []

        # So we loop from 1 to n
        for x in range(1, n + 1):
            # Check for each case, default to just the regular string representation at the end
            if (x % 3 == 0) and (x % 5 == 0):
                output.append("FizzBuzz")

            elif (x % 3 == 0):
                output.append("Fizz")

            elif (x % 5 == 0):
                output.append("Buzz")

            else:
                output.append(str(x))

        return output
