"""
Is Anagram
Problem: https://neetcode.io/problems/is-anagram?list=neetcode150

Given two strings s and t, return true if the two strings are anagrams of each other, 
otherwise return false.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCnt1 = defaultdict(int)
        charCnt2 = defaultdict(int)

        for char in range(len(s)):
            charCnt1[s[char]] += 1

        for char in range(len(t)):
            charCnt2[t[char]] += 1

        return charCnt1 == charCnt2
