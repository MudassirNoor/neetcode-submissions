class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            r = x - y
            if r == 0:
                continue
            else:
                heapq.heappush_max(stones, abs(r))

        return 0 if not stones else stones[0]