class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # sort the list first 
        sorted_list = sorted(set(nums))
        print(sorted_list)
        result = []
        if len(sorted_list) == 0:
            return 0 

        # append to a list when the difference between each is 1 

        longest = 1 
        current = 1 

        for index , i in enumerate(sorted_list):
            if index+1 < len(sorted_list):
                if sorted_list[index+1] == i + 1: 
                    current +=1 
                    longest = max(longest , current)
                else:
                    current = 1  
        
        return longest 
          

