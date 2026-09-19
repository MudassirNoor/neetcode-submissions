class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        n = len(sorted_candidates)
        result = []

        def find_combination(i, sum, combination):
            if i < n:
                sum += sorted_candidates[i]
                next = i + 1
                combination.append(sorted_candidates[i])
                if sum == target:
                    result.append(combination.copy())
                elif sum < target:
                    find_combination(next, sum, combination)

                sum -= sorted_candidates[i]
                combination.pop()
                while next < n and sorted_candidates[next] == sorted_candidates[i]:
                    next += 1
                if next < n:
                    find_combination(next, sum, combination)

        find_combination(0, 0, [])

        return result
