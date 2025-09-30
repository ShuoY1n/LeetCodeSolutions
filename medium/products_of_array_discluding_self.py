"""
Products of Array Discluding Self
Problem: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

Given an integer array nums, return an array output where output[i] is the product 
of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(1) extra space? (not counting output array)
"""

from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        sums = defaultdict()
        products = 1
        output = []
        hasZero = False

        for num in nums:
            if num == 0 and hasZero == True:
                products = 0
                break

            if num == 0:
                hasZero = True
                continue
            
            products *= num

        for num in nums:
            if num == 0 or products == 0:
                output.append(products)
                continue
            if hasZero:
                output.append(0)
                continue
            
            output.append(int(products / num))

        
        return output
