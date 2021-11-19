# First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

# So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

#     The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
#     The values are the price (in US dollars) of one share of Apple stock at that time.

# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

# Write an efficient function that takes stock_prices and 
# returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday. 

stock_prices = [10, 7, 5, 8, 11, 9]
# Returns 6 (buying for $5 and selling for $11)
stock_prices1 = [1, 2, 3]

# min_price = prices[0]
# max_profit = 0 
# loop through the list and compare (left and right) 
# 1st iteration Is 10 < 10? no
# 2nd iteration Is 10 < 7? yes | min_price = 7 
# else: max_price = price - min_price 

def get_max_profit(prices): 
    min_price = prices[0]
    max_profit = 0

    for price in prices: # 2, 1, 3
        if price < min_price: # Is 2 < 2? no, 2 < 1? yes, 1 < 3? no
            min_price = price
        else: 
            max_profit = max(max_profit, price - min_price)
    return max_profit

print(get_max_profit(stock_prices))
print(get_max_profit(stock_prices1))

# Time: O(n)
# Space: O(1)
