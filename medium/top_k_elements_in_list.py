"""
Top K Elements in List
Problem: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

Given an integer array nums and an integer k, return the k most frequent elements 
within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for index in range(len(nums)):
            hMap[nums[index]] += 1

        for key in hMap:
            buckets[hMap[key]].append(key)
        
        i = 0
        output = []
        for bucket in reversed(buckets):

            for j in bucket:
                if i == k: return output
                output.append(j)
                i+=1
        return output
