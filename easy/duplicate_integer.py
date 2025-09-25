"""
Duplicate Integer
Problem: https://neetcode.io/problems/duplicate-integer?list=neetcode150

Given an integer array nums, return true if any value appears more than once in the array, 
otherwise return false.
"""

from typing import List
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = defaultdict(int)
        
        for num in nums:
            numCount[num] += 1

            if numCount[num] > 1: return True

        return False
