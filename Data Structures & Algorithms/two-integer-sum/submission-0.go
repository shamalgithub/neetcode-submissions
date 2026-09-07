func twoSum(nums []int, target int) []int {

	numMap := make(map[int]int , len(nums))
	

	for idx , element := range nums {
		remainder := target - element 
		value , exists := numMap[remainder]
		if exists {
			return []int{value , idx}

		} else {
			numMap[element] = idx
		}
		
	}
	return []int{}

}
