
func isAnagram(s string, t string) bool {
    s_array := make([]string , 0)
    t_array := make([]string , 0)

    for _ , element := range s {
        s_array = append(s_array , string(element))
    }

    for _ , element := range t {
        t_array = append(t_array , string(element))
    }

    sort.Strings(s_array)
    sort.Strings(t_array)

    if len(s_array) == len(t_array){
        for i := range s_array {
    if s_array[i] != t_array[i] {
        return false
        }
    }
    return true
    }else{
        return false 
    }


    
    
}
