"""
LeetCode 119: Pascal's Triangle II
Problem: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Approach: Recursively build the previous row, then create the current row
using adjacent sums from the previous row.
Time: O(rowIndex^2)
Space: O(rowIndex^2) due to recursion and row creation
"""
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
      
        if rowIndex == 0:
            return [1]
          
        prev_row = self.getRow(rowIndex - 1)
        curr_row = [1]
        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i + 1])
        curr_row.append(1)
        return curr_row
