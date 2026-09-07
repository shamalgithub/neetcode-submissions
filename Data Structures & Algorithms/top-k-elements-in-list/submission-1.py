from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # use the Counter class 

        # nums_count = [(x numbner : appread y times)] # sorted in desending order 
        num_count = Counter(nums)

        counter = 0 
        result = []
        top_k = num_count.most_common(k)
        return [i[0] for i in top_k]

        


        




        

        