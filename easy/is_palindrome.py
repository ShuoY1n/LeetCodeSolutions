"""
Is Palindrome
Problem: https://neetcode.io/problems/is-palindrome?list=neetcode150

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isLetters(c):
            return ord('a') <= ord(c) and ord('z') >= ord(c) or ord('0') <= ord(c) and ord('9') >= ord(c) 

        s = s.lower()
        s = "".join(char for char in s if isLetters(char))
        left = 0
        right = len(s) - 1
        
        while (left <= right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True
