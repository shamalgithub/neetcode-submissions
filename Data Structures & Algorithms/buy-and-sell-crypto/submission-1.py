class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 

        left_p = 0 

        for right_p in range(len(prices)):
            print("left" , left_p)
            sell_value  = prices[right_p]
            buy_value = prices[left_p]

            current_profit = sell_value - buy_value 
            print(current_profit)

            if current_profit > max_profit :
                max_profit = current_profit 
            
            if buy_value > sell_value :
                left_p = right_p 
        
        return max_profit 
        