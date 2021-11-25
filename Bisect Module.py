# Bisect Module=====
# If use bisect than we need list should be sorting.....

#======== code - 1 ===========
# import bisect
#
# number = 5
#
# a = [1, 2, 4, 6, 7, 8, 9, 23]
#
# print(bisect.bisect(a, number))  # show where to insert
# bisect.insort(a, number)  # insort add value..update list
# print(a)


# ============ code - 2 ===========

import bisect

number = 334

b = [1,2,3,41,5,7,9,20,30,40]
print(bisect.bisect(b, number)) # show 10 position
bisect.insort(b, number)
print(b)