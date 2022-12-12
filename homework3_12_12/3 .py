# кстати, классная задача))) ставлю лайк
# алгоритм расписала, в мейне запустила, работает как часы, весь трюк в том, чтобы использовать очередь и перезаписывать ее,
# тогда можно найти среднее значение на каждой глубине
# сложность O(N^2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def averageOfLevels(root):                        # на вход подаю корень
        queue = [root]                             # создаю очередь, в ней пока что только корень
        result = []                                 # список результата пока пустой
        while queue:                                # пока очередь не пустая
            result.append(sum([node.val for node in queue] )/ len(queue))    # в результат добавляю сумму узлов из очереди (на этом шаге в очереди всегда будут узлы с одной глубины)

            new_queue = []             # создаю новую пустую очередь
            for node in queue:         # в нее добавляю детей всех узлов, что были в изначальной очереди, то есть все узлы на уровень глубже
                if node.left: new_queue.append(node.left)
                if node.right: new_queue.append(node.right)
            queue = new_queue       # теперь работаю с новой очередью и так далее пока совсем не останется узлов и не достигнется None во всех детях
        return result

# сейчас создам такое дерево
"""
            2
        3       9
               8  20
        Ответ должен быть 2, 6, 14
"""
def main():
    five = TreeNode(20, None, None)
    four = TreeNode(8, None, None)
    three = TreeNode(9, four, five)
    two = TreeNode(3, None, None)
    one = TreeNode(2, two, three)
    print(TreeNode.averageOfLevels(one))

main()