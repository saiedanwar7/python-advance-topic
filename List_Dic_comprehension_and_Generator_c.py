"""
List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehensions

"""
#====== List Comprehension ==============

# list_1 = [1, 32, 3, 4, 45, 4, 4, 6, 34, 12, 21, 27, 30, 11, 10]
# divide_by_3 = []
# for item in list_1:
#     if item%3 == 0:
#         divide_by_3.append(item)
# print("Without using list Comprehensions",divide_by_3)
# print("Using List Comprehension", [item for item in list_1 if item%3 == 0])
        #  [(expression) for (data) in (collection) if (condition)]


# if we add condition in one line look what happen
#syntex:
#    [(expression) for (data) in (collection) if (condition)]
# that mean:
#          (values) = []
#          for (data) in (collection):
#                   if(condition):
#                        (values).append((expression))

# ============= Dictionary Comprehension ========

# dic = {'1':'a', '2':'b', '3':'c'}
# print(dic.keys())  # dict_keys(['1', '2', '3'])
# print(dic.values()) # dict_values(['a', 'b', 'c'])
# print(dic.items()) # dict_items([('1', 'a'), ('2', 'b'), ('3', 'c')])
#
# for key,value in dic.items():
#     print("Without Dictionary Comprehension:", key, value*2)
#
#
# square_of_values = {key:value*2 for (key,value) in dic.items()}
# print(square_of_values)

#========= 2nd code Dictionary Comprehension ========
#
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
#
# dict = {key:value for key,value in zip(a,b)} #create  dictionary
# print(dict)




#========== zip() ==========
# zip() work on minimum number of element
#
# numberList = [1, 2, 3]
# strList = ["one", "two", "three", "four"]
# print(dict(zip(numberList, strList))) # {1: 'one', 2: 'two', 3: 'three'}
# # here zip print only there because win submit keys = 3
#
# strList = ["one", "two",]
# print(dict(zip(numberList, strList)))


#======== Set Comprehension ============
""" {expression for variable in collection} """
set1 = {1, 2, 1, 0}
for s in set1:
    print(s)

print(type(set1))


print("Using Set Comprehension: ",{s for s in [1,2,1,0]})
# Using Set Comprehension:  {0, 1, 2}

print({s**2 for s in [1,2,1,0]})
# {0, 1, 4}

print({s**2 for s in range(10)})

print({s for s in [1, 2, 3] if s % 2})

print({(m, n) for n in range(2) for m in range(3, 5)})
