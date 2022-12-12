# понять, зациклен ли связный список
# сложность O(N)


class ListNode:
    def __init__(self, x, nex):
        self.val = x
        self.next = nex

    def set_cycle(self, node):      # добавила сеттер, чтобы добавлять циклы нормально, в мейне как раз использую
        self.next = node

    @staticmethod
    def hasCycle(head):             # подаем на вход начало
        if head == None:            # если начало none - то не зациклен
            return False
        elif head.next == None:     # если нет следующего узла, то есть всего 1 узел, вернем false (не зациклен)
            return False

        pointer = head              # создаем указатель, который явл начальным узлом
        while pointer != None:           # пока указатель существует
            if pointer.val == None:         # проверяем, не равно ли значение None
                return True                 # если равно, то вернем тру (есть цикл)
            else:                           # иначе
                pointer.val = None          # устанавливаем значение в None
                pointer = pointer.next       # указатель теперь на следующем узле
        return False                        #если ничего не вернулось, значит цикла нет


def main():
    four = ListNode(4, None)
    three = ListNode(0, four)
    two = ListNode(2, three)
    one = ListNode(3, two)
    four.set_cycle(two)
    print(ListNode.hasCycle(one))


main()
