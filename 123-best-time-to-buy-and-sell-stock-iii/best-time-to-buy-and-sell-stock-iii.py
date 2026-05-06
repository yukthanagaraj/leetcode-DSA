class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1  = float('inf')   # min price for first buy
        sell1 = 0              # max profit after first sell
        buy2  = float('inf')   # min effective price for second buy
        sell2 = 0              # max profit after second sell

        for price in prices:
            buy1  = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2  = min(buy2, price - sell1)   # offset by profit already banked
            sell2 = max(sell2, price - buy2)

        return sell2