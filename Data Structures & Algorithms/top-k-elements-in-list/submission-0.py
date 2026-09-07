from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = Counter(nums)
        counter = 0 
        result = []
        for i in num_count.most_common():
            # i = (number x : appeared y times )
            if counter <= k-1: 
                result.append(i[0])
                counter+=1 
            else:
                break 
        
        return result 
        


        




        

        