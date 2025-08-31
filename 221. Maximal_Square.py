Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

#################################################### Brute Force ########### T.C -- O(m * n * min(m, n)^2)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, col = len(matrix), len(matrix[0])
        max_side = 0

        for i in range(rows):
            for j in range(col):
                if matrix[i][j]== '1':
                    side  = 1
                    valid = True
                    # try to expan square
                    while i + side < rows and j + side < col and valid:
                        for k in range(j, j+side+1):
                            if matrix[i+ side][k]=='0':
                                valid = False
                                break

                        for k in range(i, i+ side):
                            if matrix[k][j+ side] == '0':
                                valid = False
                                break
                        if valid:
                            side +=1
                    max_side = max(max_side, side)

        return max_side* max_side


#####################################  D .P solution   #####################  T.C --- O(m*n)------2D table

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, col = len(matrix), len(matrix[0])
        dp= [[0]* (col + 1) for _ in range(rows +1)]
        max_side = 0

        for i in range(1, rows + 1):
            for j in range (1, col +1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j]= 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
