"""
Validate Parentheses
Problem: https://neetcode.io/problems/validate-parentheses/history

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        s_arr = list(s)
        stack = []
        idx = 0
        s_length = len(s_arr)

        while idx < s_length:
            if s_arr[idx] != ']' and s_arr[idx] != ')' and s_arr[idx] != '}':
                stack.append(s_arr[idx])
                idx+=1
            else:
                if not stack:
                    return False

                match stack.pop():
                    case '(':
                        if s_arr[idx] != ')':
                            return False
                    case '[':
                        if s_arr[idx] != ']':
                            return False
                    case '{':
                        if s_arr[idx] != '}':
                            return False
                idx +=1

        return not stack
        

