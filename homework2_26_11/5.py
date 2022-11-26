# пройтись по всем элементам, сразу добавлять 1 к счетчику, когда только встала на элемент. Потом идти дальше и
# проверять, что разница между i-тым и предыдущим == 1. Если это так, то в массив добавлять значение i - 1, потом сложить все эл массива
# сложность O(n)


def getDescentPeriods(prices):
    n = len(prices)
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = 1
        if prices[i] == prices[i - 1] - 1:
            dp[i] += dp[i - 1]

    return sum(dp)


print(getDescentPeriods([3, 2, 4]))