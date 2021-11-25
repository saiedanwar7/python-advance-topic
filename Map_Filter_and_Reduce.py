# Map function

"""map(function_to_apply, list of inputs)"""

#=====Normal way ========
#
# h1 = [1, 2, 3, 4, 5, 7]
# sq = []
#
# for item in h1:
#     sq.append(item**2)  # [1, 4, 9, 16, 25, 49]
#
# print(sq)

#======== Using Map function ==============

#
# def square(n):
#     return n**2
# h1 = [1, 2, 3, 4, 5, 7]
#
# sq = list(map(square, h1))  # output [1, 4, 9, 16, 25, 49]
# print(sq)
#


# Filter
""" f """
#
# def greater_than_2(n):
#     if n>2:
#         return True
#     else:
#         return False
#
# h1 = [1, 2, 3, 4, 5, 7, 9, -2, -3]
#
# greater_2 = list(filter(greater_than_2, h1))  # output [3, 4, 5, 7, 9]
# print(greater_2)


#====Reduce ==========

from functools import reduce

def sum_num(a, b):
    return a + b

li1 = reduce(sum_num, [1, 2, 3, 4])  #  Output = 10
print(li1)



