class Solution:
    def climbStairs(self, n: int) -> int:
        possibilities = []
        i = 0
        while i < n:
            if i == 0:
                possibilities.append(1)
            elif i == 1:
                possibilities.append(2)
            else:
                possibilities.append(possibilities[i-1] + possibilities[i-2])
            
            i += 1
        
        return possibilities.pop()