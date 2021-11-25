'''
Iterable -
Iterator -
Iteration -
 '''

#generator

#Normal Example..
# a = range(3)
# print(a)
#     #output - range(0, 3)
# for i in a:
#     print(i)

# Now use Generator...
#
# def gen(n):
#     for i in range(n):
#         yield i
#
# data = gen(5)  # here create generator object..
# print(data) # <generator object gen at 0x02F226B8>
#
# print(next(data)) # here we create 5 number of generator
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
#


#========= Iterable =========

# num = 345
# for i in num:
#     print(i)
    # here this code is show error(TypeError: 'int' object is not iterable)
    # only string is iterable

# num = "Saied"
# for i in num:
#     print(i)

# another example
num = "Saied"
iter1 = iter(num)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))