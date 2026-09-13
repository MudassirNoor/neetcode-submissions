class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        match_set = {}
        w1 = 0
        w2 = len(s1)
        
        for c in s1:
            if c not in match_set:
                match_set[c] = 1
            else:
                match_set[c] += 1
    
        compare_set = {}
        while w2 <= len(s2):
            if not compare_set:
                window = s2[w1:w2]
                for c in window:
                    if c not in compare_set:
                        compare_set[c] = 1
                    else:
                        compare_set[c] += 1
            else:
                if s2[w2-1] in compare_set:
                    compare_set[s2[w2-1]] += 1
                else:
                    compare_set[s2[w2-1]] = 1

            isPermutation = True
            for key, val in match_set.items():
                if key not in compare_set or compare_set[key] != val:
                    isPermutation = False
                    break
            
            if isPermutation:
                return True
            else:
                if compare_set[s2[w1]] > 1:
                    compare_set[s2[w1]] -= 1
                else:
                    compare_set.pop(s2[w1])
                w1 += 1
                w2 += 1
            
        return False