"""
Valid Sudoku
Problem: https://neetcode.io/problems/valid-sudoku?list=neetcode150

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numMapRow = defaultdict(int)
        numMapCol = defaultdict(int)
        numMapSquare = defaultdict(int)

        for row in board:
            numMapRow.clear()
            for num in row:
                if num == ".": 
                    continue
                if numMapRow[num] != 0:
                    return False
                numMapRow[num] += 1

        colIndex = 0
        while colIndex < 9:
            numMapCol.clear()
            for row in board:
                if row[colIndex] == ".": 
                    continue
                if (numMapCol[row[colIndex]] != 0):
                    return False
                numMapCol[row[colIndex]] += 1
            colIndex += 1

        x = 0
        y = 0

        while x < 7:
            y = 0
            while y < 7:
                numMapSquare.clear()
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:   
                        if board[j + y][i + x] == ".": 
                            j+=1
                            continue
                        if numMapSquare[board[j + y][i + x]] != 0:
                            return False
                        numMapSquare[board[j + y][i + x]] += 1
                        j+=1
                    i+=1
                y+=3
            x+=3

        return True
