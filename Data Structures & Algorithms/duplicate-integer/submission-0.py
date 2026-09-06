class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_map = {}
        for n in nums:
            if n in set_map:
                return True
            set_map[n] = 1

        return False 