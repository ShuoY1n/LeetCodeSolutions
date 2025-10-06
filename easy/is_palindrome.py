"""
Is Palindrome
Problem: https://neetcode.io/problems/is-palindrome?list=neetcode150

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        while (left <= right):
            if (not (ord(s[left]) >= ord('a') and ord(s[left]) <= ord('z') or ord(s[left]) >= ord('0') and ord(s[left]) <= ord('9'))):
                left += 1
                continue
            if (not (ord(s[right]) >= ord('a') and ord(s[right]) <= ord('z') or ord(s[right]) >= ord('0') and ord(s[right]) <= ord('9'))):
                right -= 1
                continue
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True
