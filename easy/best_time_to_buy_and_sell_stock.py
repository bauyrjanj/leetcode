def max_profit(arr):
    profit = 0
    min_price = max(arr)

    for price in arr:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    # prices = [7, 6, 4, 3, 1]

    print(max_profit(prices))



