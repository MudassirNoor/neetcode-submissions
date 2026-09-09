class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subset = []
            for subset in result:
                # Make a new subset by adding the currrent number to each existing subset
                new_subset.append(subset + [num])
            result.extend(new_subset)
        
        return result