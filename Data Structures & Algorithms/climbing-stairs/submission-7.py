class Solution:
    def climbStairs(self, n: int) -> int:
        possibilities = []
        
        for i in range(n):
            if i == 0:
                possibilities.append(1)
            elif i == 1:
                possibilities.append(2)
            else:
                possibilities.append(possibilities[i-1] + possibilities[i-2])
        
        return possibilities.pop()