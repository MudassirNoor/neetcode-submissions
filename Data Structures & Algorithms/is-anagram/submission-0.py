class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not s and not t) or len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1
            
            if t[i] not in t_map:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] += 1

        for key, val in s_map.items():
            if key not in t_map or t_map[key] != val:
                return False

        return True