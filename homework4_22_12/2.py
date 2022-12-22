# вычислить наименьшую разницу между значениями узлов
# сложность O(N)

class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r


def getMinimumDifference(root):
    vals = []
    getValues(root, vals).sort()        # все значения в список


    diff = None                         # ответ пока что ничего
    for i in range(len(vals)-1):        # прохожусь по значениям до предпоследнего
        cal = abs(vals[i+1]-vals[i])    # разницу следующего и итого записываем в переменную
        if diff is None:                # если первая итерация, то дифф = переменной
            diff = cal
            continue
        if cal < diff:                 # если разница между эл меньше дифф
            diff = cal                  # перезапишем дифф
    return diff


def getValues(root, vals):
    if not root:
        return

    vals.append(root.val)

    if root.left:
        getValues(root.left, vals)

    if root.right:
        getValues(root.right, vals)

    return vals


def main():
    five = TreeNode(3, None, None)
    four = TreeNode(1, None, None)
    three = TreeNode(6, None, None)
    two = TreeNode(2, four, five)
    one = TreeNode(4, two, three)

    print(getMinimumDifference(one))

main()