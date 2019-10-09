# https://leetcode.com/problems/defanging-an-ip-address/

"""
Description
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # A lot of these problems seem so trivial with Python. I'm not sure if they are supposed to be this easy or maybe they are more difficult in other languages.
        return address.replace('.', '[.]')
