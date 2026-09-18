class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        cooldown = 0
        for  price in prices[1:]:

            prevHold = hold
            prevSold = sold
            prevCooldown = cooldown

            hold = max(prevHold, prevCooldown - price)
            sold = prevHold + price
            cooldown = max(prevSold, prevCooldown)

        return max(sold, cooldown)