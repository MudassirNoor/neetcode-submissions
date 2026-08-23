class Solution:
    # O(n) complexity
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        currentMax  = 0
        for num in nums:
            if num == 1:
                currentMax = currentMax + 1

            if currentMax > maxConsecutive:
                maxConsecutive = currentMax

            if num == 0:
                currentMax = 0
   
        return maxConsecutive