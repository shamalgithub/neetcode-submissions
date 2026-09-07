func hasDuplicate(nums []int) bool {
   // create a set 

   set := make(map[int]struct{})
   for _ , element := range nums {
    set[element] = struct{}{}
   }

   if len(set) != len(nums){
    return true
   } else {
    return false
   }
    
}
