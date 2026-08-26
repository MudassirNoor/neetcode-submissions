class Solution:
    _delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for string in strs:
            if string:
                encoded_str = encoded_str + str(len(string)) + self._delimiter + string 
            else:
                encoded_str = encoded_str + str(0) + self._delimiter
        
        return encoded_str
 
    def decode(self, s: str) -> List[str]:
        decoded_str = []

        if not s:
            return decoded_str
        
        start = 0
        delimiter_idx = 0
        while delimiter_idx < len(s):
            if s[delimiter_idx] != self._delimiter:
                delimiter_idx += 1
            else:
                string_length = int(s[start:delimiter_idx])
                if string_length > 0:
                    start_idx = delimiter_idx + 1
                    decoded_str.append(s[start_idx:string_length + start_idx])
                else:
                    decoded_str.append("")
                delimiter_idx += string_length + 1
                start = delimiter_idx


        return decoded_str