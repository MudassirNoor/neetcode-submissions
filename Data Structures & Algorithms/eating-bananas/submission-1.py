class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed <= max_speed:
            s = (min_speed + max_speed) // 2
            totalTime = 0

            for bananas in piles:
                totalTime += math.ceil(bananas/s)
            
            if totalTime > h:
                min_speed = s + 1
            else:
                max_speed = s - 1
        
        return min_speed