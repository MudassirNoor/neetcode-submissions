class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in nums]
        houses = len(nums) - 1
    
        for h in range(houses, -1, -1):
            if h > houses - 2:
                cache[h] = nums[h]
            else:
                a = cache[h + 2]
                if h + 3 <= houses:
                    cache[h] = nums[h] + max(a, cache[h + 3])
                else:
                    cache[h] = nums[h] + cache[h + 2]

        if len(cache) > 1:
            return max(cache[0], cache[1])
        else:
            return cache[0]