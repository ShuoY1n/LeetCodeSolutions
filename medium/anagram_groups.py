"""
Anagram Groups
Problem: https://neetcode.io/problems/anagram-groups?list=neetcode150

Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = defaultdict(list)

        for string in strs:
            charFreq = [0] * 26
            
            for j in range(len(string)):
                charFreq[ord(string[j]) - ord('a')] += 1;

            hMap[tuple(charFreq)].append(string)

        return list(hMap.values())
