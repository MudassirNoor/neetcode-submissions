class Solution:
    def climbStairs(self, n: int) -> int:
        possibilities = [1, 2]
        
        for i in range(2, n):
            possibilities.append(possibilities[i-1] + possibilities[i-2])
        
        return possibilities[n-1]