# взяла код с пары для ограбления без учета домов в круге. по сути нужно запустить код 2 раза.
# Сначала без первого элемента, потом без последнего и вернуть максимум из результата
# я так и сделала ниже. Сложноcть O(n)


def rob(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
    return dp[-1]


array_to_check = [1,2,3]
print(max(rob(array_to_check[1:]), rob(array_to_check[:len(array_to_check) - 1])))

