class Solution:
    _delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for string in strs:
            if string:
                encoded_str = encoded_str + str(len(string)) + self._delimiter + string 
            else:
                encoded_str = encoded_str + str(0) + self._delimiter
        
        print(encoded_str)
        return encoded_str
 
    def decode(self, s: str) -> List[str]:
        decoded_str = []

        if not s:
            return decoded_str
        
        start = 0
        i = 0
        while i < len(s):
            if s[i] == self._delimiter:
                v = s[start:i]
                print(f"Before{i}")
                string_length = int(v)
                if string_length > 0:
                    start_idx = i + 1
                    decoded_str.append(s[start_idx:string_length + start_idx])
                else:
                    decoded_str.append("")
                i += string_length + 1
                print(f"After{i}")
                start = i
            else:
                i += 1


        return decoded_str