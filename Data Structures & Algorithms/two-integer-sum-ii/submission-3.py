class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashed= {}
        for i in range(len(numbers)):
            other_number = target - numbers[i]
            if other_number in hashed:
                print(hashed)
                return [hashed[other_number] + 1, i + 1]
            else:
                hashed[numbers[i]] = i