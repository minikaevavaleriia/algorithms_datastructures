# Пока параметр не равен нулю, проверяю, делится ли число на 2 без остатка (является ли четным).
# Если число четное - делю на 2. Если число нечетное, то вычитаю единицу.
# При этом после каждой итерации инкрементирую счетчик.
# Когда число станет нулем - возвращаю счетчик.
# Сложность равна O(N), где N - наименьшее количество возможных операций над числом для того, чтобы оно стало нулем.


def numberOfSteps(num):
    counter = 0                     # счетчик
    while num:                      # пока число не равно нулю
        if num % 2 == 0:            # если четное
            num /= 2                # делю на 2
            counter += 1            # инкрементирую счетчик
        else:                       # если нечетное
            num -= 1                # вычитаю единицу
            counter += 1            # инкрементирую счетчик
    return counter                  # возвращаю количество итераций


print(numberOfSteps(123))
