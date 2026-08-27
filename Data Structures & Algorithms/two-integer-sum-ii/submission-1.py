class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(0, length):
            remainder = target - numbers[i]
            left = i + 1
            right = length - 1
            # Perform binary search on the rest of the array to find
            # the complimentary number
            while left <= right:
                mid = (left + right) // 2
                if remainder > numbers[mid]:
                    left = mid + 1
                elif remainder < numbers[mid]:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]

        return [-1, -1]