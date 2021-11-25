"""
 The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

 """
# Use the format() method to insert numbers into strings:
# age = 23
# txt = "My name is John, I am {}"
# print(txt.format(age))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
item = 567
price = 49.95
myorder = "I want {} pieces of item {} for dollars"
print(myorder.format(quantity, item, price))

#use index numbers
quantity = 3
item = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, item, price))

# Using different placeholder values:
#use Attribute name
txt1 = "My name is {fname}, I'am {age}".format(fname= "Saied", age = 24)
print(txt1)

#use Values indexes
txt2 = "My name is {0}, I'am {1}".format("Saied", 24)
print(txt2)


txt3 = "My name is {}, I'am {}".format("Saied", 24)
print(txt3)




#====== Code With Harry ======================
#========Normal Way ==========

# users = ['Saimun', "sourve", "Jakir", "Salman", "Hasan"]
# computer = ["Dell", "Asus", "Acer", "Hp", "Lenevo"]
#
# for i in range(0, len(users)):
#     print("Computer used by", users[i], "is", computer[i])

# ====== Using Format =================
# users = ['Saimun', "sourve", "Jakir", "Salman", "Hasan"]
# computer = ["Dell", "Asus", "Acer", "Hp", "Lenevo"]
#
# for i in range(0, len(users)):
#     templeate = "Computer used by {} is {}"
#     print(templeate.format(users[i], computer[i]))


