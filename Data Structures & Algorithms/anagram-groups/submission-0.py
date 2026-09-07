class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sort all the strings in the list 
        # compare them and group 
        # we need to preserve the actual string 

        # use a hashmap {str : list[str]} and set the keys to the sorted string and 
        # the values to the actual string 



        sorted_strings = ["".join(sorted(i)) for i in strs]
        str_map = {}

        for index , i in enumerate(sorted_strings): 
            if i in str_map.keys(): 
                (str_map[i]).append(strs[index])
            else:
                str_map[i] = [strs[index]]

        # act : ["act" , "cat"]
        # opst : ["stop" , "pots" , "tops"]

        result = []
        for key , value  in str_map.items():
            result.append(value)
        
        return result 



        