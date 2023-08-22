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

# stocks(prices=[7,3,4,6,1])

## way better solution
def stock(prices):
    n = len(prices)
    m1 = prices[0]
    m2 = 0
    # print(n, m1, m2)
    for i in range(1, n):
        if m1 > prices[i]:
            m1 = prices[i]
        
        if m2 < (prices[i] - m1):
            m2 = prices[i] - m1

    return m2     

print(stock(prices=[7,3,4,6,1]))