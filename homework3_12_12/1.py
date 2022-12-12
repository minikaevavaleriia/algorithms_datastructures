# Я переписала задачу по-своему, добавив статический метод в класс узла списка.
# У меня действительно реализован связанный список, но задать его динамически или сгенирировать я не захотела.
# функция isPalindrome работает с моими списками разного размера корректно.
# сложность O(n), где n - кол-во узлов(длина списка)

class ListNode:
    def __init__(self, val=0, next_=None):       # инит из условия
        self.val = val
        self.next_ = next_
    @staticmethod
    def isPalindrome(li):                       # на вход подаю связанный список
        nums = []                               # создаю пустой список, чтобы хранить значения узлов
        while li[0] is not None:                # если значение первого элемента есть
            nums.append(li[0].val)              # то в список добавляю это значение
            li[0] = li[0].next_                 # дальше в элемент записываю следующий узел
        return nums == nums[::-1]               # после того как пройдусь по всем узлам и запишу их значение в список,
                                                # возвращаю true или false (если палиндром или если нет)

def main():
    five = ListNode(2, None)
    four = ListNode(3, five)
    three = ListNode(0, four)
    two = ListNode(3, three)
    one = ListNode(2, two)
    linkedlist = [one, two, three, four]
    print(ListNode.isPalindrome(linkedlist))

main()