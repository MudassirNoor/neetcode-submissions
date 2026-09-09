class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        length = len(nums)

        def findSubset(i, subset):
            if i >= length:
                return
            
            subset.append(nums[i])
            result.append(subset.copy())
            
            findSubset(i + 1, subset) 
            subset.pop()
            findSubset(i + 1, subset)

            
        findSubset(0, [])

        return result