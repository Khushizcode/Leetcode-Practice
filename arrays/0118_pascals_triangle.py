"""
LeetCode 118: Pascal's Triangle
Problem: You are given an integer numRows.Return the first numRows of Pascal's triangle.
Approach: Recursively build numRows - 1 rows, then create the current row
using adjacent sums from the previous row.
Time: O(n^2)
Space: O(n^2)
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        triangle = self.generate(numRows-1)
        prev_row = triangle[-1]
        curr_row = [1]
        for i in range(len(prev_row)-1):
            curr_row.append(prev_row[i]+prev_row[i+1])
        curr_row.append(1)
        triangle.append(curr_row)
        return triangle
        
