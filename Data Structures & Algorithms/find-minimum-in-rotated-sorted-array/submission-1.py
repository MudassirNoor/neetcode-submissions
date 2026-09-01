class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        
        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] and nums[mid] < nums[right]:
                break
            
            elif nums[mid] > nums[right]:
                left = mid + 1
    
            else:
                right = mid
            
        return nums[left]