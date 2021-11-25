# Lambda functions can take any number of arguments:
"""
Syntax:
lambda agrgument: manipulate(argument)

Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

"""
# ======= normal ways =======
# def add(a, b):
#     s = a + b
#     return s
# print(add(4, 6))
#
# # ======== Using Lambda =========
# add = lambda x, y : x + y
# print(add(4, 16))

# ========= using lambda on list sorting ======

# a = [(1, 2), (4, 5), (555, 34)]
# a.sort(key = lambda x : x[1])
#
# print(a)
#============================
# def x (val):
#     return val[1]
# a = [(1, 2), (4, 5), (555, 34)]
# a.sort(key = x)
#
# print(a)



#========== w3schoool =============

# x = lambda a : a + 10
# print(x(5))
#
# y = lambda a, b : a * b
# print(y(5, 6))
#
# z = lambda a, b, c : a + b + c
# print(z(2,3,4))

# =========== code - 1 =============

# def myfunc(n):
#     return lambda a : a * n
#
# mydoubler = myfunc(2)
# print(mydoubler(11))  # 22

# ======== code - 2 =========

# def myfun(n):
#     return lambda a: a - n
# mynum = myfun(20)
# print(mynum(11))  # -9
