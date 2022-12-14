# сначала генерирую массив по заданным правилам, потом беру макс элемент
# сложность O(n // 2), то есть примерно O(n)

def getMaximumGenerated(n):
    l = [0] * (n + 1)           # по условию
    if n == 0:                  # если длина массива 0,
        return 0                # то возвращаю 0
    l[1] = 1                    # по условию
    for i in range(1, (n + 1) // 2):   # прохожусь от 1 до (длина массива + 1) индекса деленного нацело на 2, потому что ниже мы обращаемся к
                                        # l[2 * i + 1] элементу. Нельзя выходить за пределы. А это как раз последний элемент массива при максимальном i
        l[2 * i] = l[i]
        l[2 * i + 1] = l[i] + l[i + 1]
    print(l)                    # просто вывела для себя, чтобы проверить
    return max(l)               # возвр макс эл


print(getMaximumGenerated(7))
