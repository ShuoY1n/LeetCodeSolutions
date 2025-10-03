"""
Longest Consecutive Sequence
Problem: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150

Given an unsorted array of integers nums, return the length of the longest consecutive sequence.
You must write an algorithm that runs in O(n) time.
"""

from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nmap = defaultdict(int)
        length = 1
        current_seq = []
        next_seq = []

        if len(nums) == 0: return 0

        for num in nums:
            nmap[num]+=1
        
        for num in nums:
            if nmap[num + 1] != 0:
                next_seq.append(num + 1)
        if len(next_seq) == 0: return length
            
        
        while True:
            if len(next_seq) == 0: break
            current_seq = next_seq.copy()
            next_seq.clear()
            for num in current_seq:
                if nmap[num + 1] != 0:
                    next_seq.append(num + 1)
            length += 1
        return length
