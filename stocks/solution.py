def stocks(prices):
    temp = []
    mini = min(prices)
    index = prices.index(mini)

    for price in range(index, len(prices)):
        temp.append(prices[price])

    maxi = max(temp)
    profit = maxi - mini
    if profit <= mini:
        profit = 0

    print(profit)

stocks(prices=[7,3,4,6,1])