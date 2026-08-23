class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0

        i = 0
        k = length
        
        for i in range(0, length):
            if nums[i] == val:
                k = i
                break

        for i in range (k+1, length):
            if nums[i] != val:
                tmp = nums[i]
                nums[i] = val
                nums[k] = tmp
                k += 1
        
        return k
