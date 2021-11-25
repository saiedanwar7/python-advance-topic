# * args and **kwargs tutorial
# here args or kwargs name is not important we use here anything...only important is (*)/(**) star...



#========= 1st example of *args =====================

# def function_1(*args): # here we submit some agrument, *args auto submite all argument value
#     print(type(args)) # *args is tuple type data
#     print("The name of the student is ",args[0], "and age is ", args[1], "and rollno is ", args[2])
#
#
# function_1("Saied", 24, 1168)

#=========== 2nd example of *agrs ===========
# def function_1(*args): # here we submit some agrument, *args auto submite all argument value
#     if(len(args) == 3):
#         print("The name of the student is",args[0], "and age is ", args[1], "and rollno is ", args[2])
#     else:
#         print("The name of the student is ",args[0], "and age is ", args[1]) #if user submit 2 value
#
# function_1("Saied", 24)

#============== 3rd example of *args =================
#
# def function_1(*args): # here we submit some agrument, *args auto submite all argument value
#     if(len(args) == 3):
#         print("The name of the student is",args[0], "and age is ", args[1], "and rollno is ", args[2])
#     else:
#         print("The name of the student is ",args[0], "and age is ", args[1]) #if user submit 2 value
#
# msl = ("hasan", 25, 1231)  # create object and submit user value as your wish
# function_1(*msl)  # here use * ster before object...when function call
#


#========== **kwargs =========================
def function_1(*args):

    if(len(args) == 3):
        print("The name of the student is", args[0], "and age is",args[1], "and rollno is",args[2])
    else:
        print("The name of the student is", args[0], "and age is", args[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

def master(normal, *args, **kwars):

    print(normal)
    for i in args:
        print(i)
    for key, value in kwars.items():
        print(key, value)


msl =("harry", 22, 1212)
marklist = {"Saimun": 100, "rohan das": 97, "Jakir": 91, "sourve": 80, "Salman": 70}

# printmarks(**marklist)

#print(master("normal arg", *msl, **marklist))  # here it's output is come none in last line,,, because we print this function

master("normal arg", *msl, **marklist)  # here we return this function




