class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_p , right_p = 0 , len(heights) - 1 

        max_area = 0 

        while left_p < right_p :
            
            area = (right_p - left_p) * min(heights[left_p] , heights[right_p])
            
            if area > max_area : 
                max_area = area 
            
            if heights[left_p] < heights[right_p] : 
                left_p += 1 
            else:
                right_p -= 1 
            
        return max_area 

        