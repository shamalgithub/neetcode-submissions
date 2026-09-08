class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left_p = 0 

        for right_p in range(len(s2)):

            window_length = right_p - left_p +1 
       

            if window_length  > len(s1)   : # left should come forwad 
                
                left_p += 1 
                window_length = right_p - left_p + 1 # recalculate - couldnt figure out this part only  !!! 

            if window_length == len(s1):
                sorted_s1 = "".join(sorted(s1))
                sorted_s2_sub = "".join(sorted(s2[left_p : right_p+1])) 
                

                if sorted_s1 == sorted_s2_sub:
                    return True 
                
        return False 
    
