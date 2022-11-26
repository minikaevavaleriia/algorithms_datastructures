# я решила представить поле из условия в виде графа, где каждая ячейка связа со своими соседями. Таким образом,
# мне нужно взять алгоритм дейкстры с пары и на вход подать матрицу, которую я составила для примера.
# естественно на литкоде это не работает))) я вручную составила граф из примера)))

# функция может найти кол-во ходов, которые нужны, чтобы дойти до цели. но не все возможные пути запишутся
# я не знаю, где ввести счетчик на пути здесь(поэтому могу вернуть только кол-во шагов для достижения цели)
# сложность O(n^2)


def uniquePathsWithObstacles(start, matrix):
    visited = set()
    q = [start]
    path_lengths = [2 ** 32] * len(matrix)
    path_lengths[start] = 0
    path = [[start]] * len(matrix)
    while q:
        cur_node = q.pop(0)
        visited.add(cur_node)

        row = matrix[cur_node]
        for i in range(len(row)):
            if row[i] > 0 and path_lengths[i] > path_lengths[cur_node] + row[i]:
                path_lengths[i] = path_lengths[cur_node] + row[i]
                path[i] = path[cur_node] + [i]

            if row[i] > 0 and i not in visited:
                visited.add(i)
                q.append(i)
    return len(path[-1]) - 1


matrix_ = [[1, 1, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 1, 0, 0, 0],
           [1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 1, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 1, 0, 1, 1]]

print(uniquePathsWithObstacles(0, matrix_))
