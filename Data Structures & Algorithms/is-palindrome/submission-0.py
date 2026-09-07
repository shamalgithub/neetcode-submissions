class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove the space and none alphanumeric characters 
        # alnum only returns alphanumerics 
        
        combined_string = "".join([char.lower() for char in s if char.isalnum()])

        left , right = 0 , len(combined_string) - 1 
        while left < right : 
            if combined_string[left] == combined_string[right]:
                left += 1
                right -= 1  
            else:
                return False 
        return True 