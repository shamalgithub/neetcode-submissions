class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_to_open_map = {")" : "(" , "]":"[" , "}":"{"}

        for char in s: 
            if char in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[char]:
                    print("poping from stack")
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)
        
        if not stack: 
            return True
        else:
            return False 


