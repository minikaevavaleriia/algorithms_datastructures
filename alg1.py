# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     arr = [1] * (n + 1)
#
#     for i in range(2, n+1):
#         arr[i] = arr[i - 1] + arr[i - 2]
#
#     return arr[-1]
#
#
# print(fibo(int(input())))


# def fib_m(n):
#     if n == 0 or n == 1:
#         return 1
#     a, b, = 1, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# print(fib_m(int(input())))

#
# def isValid1(s):
#     my_stack = []
#     for bracket in s:
#         if bracket == '(':
#             my_stack.append(bracket)
#         else:
#             if len(my_stack) == 0:
#                 return False
#             else:
#                 my_stack.pop()
#     return len(my_stack) == 0
#
#
# print(isValid1('()(())'))


# def isValid2(s):
#     my_stack = []
#     d = {'(': ')',
#          '[': ']',
#          '{': '}'}
#     for bracket in s:
#         if bracket in d:
#             #это открывающая скобка
#             my_stack.append(bracket)
#         else:
#             if len(my_stack) == 0:
#                 return False
#             else:
#                 if d[my_stack[-1]] == bracket: #проверка на правильность закрытия
#                     my_stack.pop()
#                 else:
#                     return False
#     return len(my_stack) == 0
#
#
# print(isValid2('([]{}){}'))


# def sortSentence(s):
#     words = s.split()
#     new_words = [''] * len(words)
#     for w in words:
#         new_words[(int(w[-1]) - 1)] = w[:-1]
#     return ' '.join(new_words)
#
#
# print(sortSentence('is2 sentence4 a3 This1'))


# def maxWidthOfVerticalArea(li):
#     list_ = []
#     for i in li:
#         list_.append(i[0])
#     for i in range(len(list_) - 1):
#         for j in range(1, len(list_)):
#             if i > j:
#                 list_[i], list_[j] = list_[j], list[i]

#     max0 = 0
#     max1 = 0
#     for i in range(1, len(list_)):
#         max1 = list_[i] - list_[i - 1]
#         if max1 > max0:
#             max0 = max1
#
#     print(max0)


# maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])


# def dist(point):
#     return (point[0] ** 2 + point[1] ** 2) ** 0.5
#
#
# print(dist([0, 45]))
#
#
# def bubble_sort(list_):
#     for i in range(len(list_) - 1):
#         for j in range(1, len(list_)):
#             if dist(list_[i]) > dist(list_[j]):
#                 list_[i], list_[j] = list_[j], list_[i]
#     return list_
#
#
# def kClosest(points, k):
#     points = bubble_sort(points)
#     return points[:k]
#
#
# print(kClosest([[1,3],[-2,2]], 1))


# def stairs(n):
#     if n == 0 or n == 1:
#         return 1
#     dp = [1] * (n + 1)
#     for i in range(2, len(dp)):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[-1]
#
#
# print(stairs(5))


# def max_subsequence(nums):
#     dp = [1] * len(nums)
#     for i in range(len(nums)):
#         max_sub = 0
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 max_sub = max(max_sub, dp[j])
#         dp[i] = max_sub + 1
#     return dp
#
#
# print(max_subsequence([8,5,10,6,12,3,24,7,8]))


# def levenstein_dist(s1, s2):
#     dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
#
#     for i in range(len(dp)):
#         dp[i][0] = i
#
#     for i in range(len(dp[0])):
#         dp[0][i] = i
#
#     for i in range(1, len(dp)):
#         for j in range(1, len(dp[0])):
#             if s1[j-1] == s2[i-1]:
#                 cost = 0
#             else:
#                 cost = 1
#             dp[i][j] = min(dp[i][j-1] + 1,
#                            dp[i-1][j] + 1,
#                            dp[i-1][j-1] + cost)
#
#     return dp[-1][-1]


# print(levenstein_dist('algo', 'aglo'))


# def backpack(W, weight, prices):
#     N = len(prices)
#     dp = [[0] * (1+W) for _ in range(N+1)]
#     for i in range(1, len(dp)):
#         for j in range(1, len(dp[0])):
#             if j - weight[i-1] >= 0:
#                 dp[i][j] = max(
#                     dp[i-1][j],
#                     dp[i-1][j-weight[i-1]] + prices[i-1]
#                 )
#     return dp[-1][-1]
#
#
# print(backpack(13, [3,4,5,8,9], [1,6,4,7,6]))


# res = []
# def generate(seq, digits):
#     if not digits:
#         res.append(seq)
#     else:
#         for i in range(len(digits)):
#             generate(seq+digits[i], digits[:i] + digits[i+1:])
#
#
# generate('', ['1', '2', '3'])
# print(res)


# res = []
#
#
# def max_subsequence_till_k(seq, digits, k):
#     if len(seq) == k:
#         res.append(seq)
#     else:
#         for i in range(len(digits)):
#             max_subsequence_till_k(seq+[digits[i]], digits[i+1:], k)
#
#
# max_subsequence_till_k([], [1,2,3,4,5], 3)
# print(res)


#генерация скобочных последовательностей
# res = []
# def brackets_generate(seq, n, opened, closed):
#     if len(seq) == n:
#         res.append(seq)
#     else:
#         if closed < opened:
#             brackets_generate(seq+')', n, opened, closed+1)
#         if opened != n//2:
#             brackets_generate(seq+'(', n, opened+1, closed)
#
# brackets_generate(seq='', n=10, opened=0, closed=0)
#
# print(res)


# def stairs(n):
#     if n == 0 or n == 1:
#         return 1
#     dp = [1] * (n + 1)
#     for i in range(3, len(dp)):
#         dp[i] = dp[i - 1] + dp[i - 3]
#     return dp[-1]
#
#
# print(stairs(100))


# def stairs24(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 0
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[2] = 1
#     for i in range(4, len(dp)):
#         dp[i] = dp[i - 2] + dp[i - 4]
#     return dp
#
#
# print(stairs24(12))


# def stairs(n):
#     if n == 0 or n == 1:
#         return 1
#     dp = [1] * (n + 1)
#     for i in range(2, len(dp)):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp
#
#
# print(stairs(12))


# def rob(nums):
#     dp = [0] * len(nums)
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     for i in range(2, len(dp)):
#         dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
#     return dp[-1]
#
# print(rob([12,2,7,33,1]))


# def pascal_piramid













