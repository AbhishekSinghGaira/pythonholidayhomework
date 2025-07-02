#Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

prices = eval(input("Enter the price of the stocks"))

buy_price = prices[0]

max_profit = 0
for i in range(1, len(prices)):
         max_profit = max(max_profit, prices[i] - buy_price)
         buy_price = min(buy_price, prices[i])


print('max profit', max_profit)

            