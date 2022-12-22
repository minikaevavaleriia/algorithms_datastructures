# как фибоначи только считаем сумму трех предыдущих
# сложность O(n)
def tribonacci(n):
    f = [0, 1, 1]

    while len(f) < n + 1:
        f += [f[-1] + f[-2] + f[-3]]

    return f[n]

print(tribonacci(25))