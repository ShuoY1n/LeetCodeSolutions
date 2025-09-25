"""
Two Integer Sum
Problem: https://neetcode.io/problems/two-integer-sum?list=neetcode150

Given an array of integers nums and an integer target, return the indices i and j 
such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        intMap = defaultdict(int)
        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]

            if intMap[diff] != 0: return [intMap[diff] - 1, i]
            intMap[nums[i]] += i + 1
