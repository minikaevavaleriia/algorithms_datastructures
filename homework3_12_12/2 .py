# алгоритм перевода расположен под кодом, я смогу вам его объяснить, там происходят сдвиги и добавление бита,
# чтобы решить задачу, я по сути делаю все наоборот
# сложность O(n), где n - кол-во узлов(длина списка)


class ListNode:
    def __init__(self, val=0, next_=None):       # инит из условия
        self.val = val
        self.next_ = next_


    @staticmethod
    def getDecimalValue(li):
        answer = 0
        while li[0]:
            answer = 2 * answer + li[0].val
            li[0] = li[0].next_
        return answer


def main():
    three = ListNode(1, None)
    two = ListNode(0, three)
    one = ListNode(1, two)
    linkedlist = [one, two, three]
    print(ListNode.getDecimalValue(linkedlist))

main()

"""
Take For Example:
1101 -> 13

Binary View
0000 * 2 # shift left
0000 + 1 # add bit

0001 * 2 # shift left
0010 + 1 # add bit

0011 * 2 # shift left
0110 + 0 # add bit

0110 * 2 # shift left
1100 + 1 # add bit

1101 # 13

Decimal View
0 * 2 # x2
0 + 1 # add bit

1 * 2 # x2
2 + 1 # add bit

3 * 2 # x2
6 + 0 # add bit

6 * 2 # x2
12 + 1 # add bit

13 # Answer
"""