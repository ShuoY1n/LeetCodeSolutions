"""
Three Integer Sum
Problem: https://neetcode.io/problems/three-integer-sum/history

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        sub_arr = []

        idx = -1
        for num in nums:
            idx += 1
            curr_sum = -num
            p1 = idx + 1
            p2 = len(nums) - 1

            while p1 < p2:
                if nums[p1] + nums[p2] > curr_sum:
                    p2-=1
                elif nums[p1] + nums[p2] < curr_sum:
                    p1+=1
                elif p1 == p2:
                    return []
                else:
                    sub_arr = [nums[p1], nums[p2], num]
                    if sub_arr in out:
                        p1+=1
                        p2-=1
                        continue
                    out.append(sub_arr)
                    p1+=1
                    p2-=1
        return out

