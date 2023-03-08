def solution(price, money, count):
    priceList = [price * i for i in range(1, count+1)]
    return sum(priceList) - money if sum(priceList) - money > 0 else 0