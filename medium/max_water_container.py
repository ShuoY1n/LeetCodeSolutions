"""
Max Water Container
Problem: https://neetcode.io/problems/max-water-container/history

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        curr_max = 0

        while p1 < p2:
            curr = min(heights[p1], heights[p2]) * (p2 - p1)
            
            if curr > curr_max:
                curr_max = curr
            
            if heights[p1] < heights[p2]:
                p1+=1
            else:
                p2-=1
        return curr_max
        

