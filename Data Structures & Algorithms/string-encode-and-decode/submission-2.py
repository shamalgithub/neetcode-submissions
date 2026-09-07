class Solution:

    def encode(self, strs: List[str]) -> str:
        # algorithm -> delimeter number+special character

        encoded_string = "".join(f"{len(s)}#{s}" for s in strs) 
        # print(encoded_string)
        return encoded_string 
        #['hat' , 'most' , 'do']
        # result 3#hat4#most2#do
        # 1#0

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the '#' that ends the length prefix
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])       # e.g. "10" -> 10
            word = s[j+1 : j+1+length] # grab exactly `length` characters
            result.append(word)
            
            i = j + 1 + length          # jump straight past this word
        
        return result


            


