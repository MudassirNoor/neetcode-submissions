class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [0, 0]

        for n in nums:
            currentMax = max(robbed[0] + n, robbed[1])
            robbed[0] = robbed[1]
            robbed[1] = currentMax

        return robbed[1] 