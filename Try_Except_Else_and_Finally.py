

#======== try example ===========
# try:
#     open("this.txt")
# except Exception as e:
#     pass
#
# print("Program is alive")

# ======== 2nd code ==========
# try:
#     file = open("this.txt", "r")
# except EOFError as e:
#     print("eof error")
# except IOError as e:
#     print("we can handle this error")
# finally:
#     print("This will be printed irrespective of the exception occurrence")


# =============== 3rd code ===============
# serial of exception = try -> except -> else -> finally (finally always print in last line of on code)

try:
    print("I will try this code and will throw exception if there is any problem")
except Exception as e:
    print("I will run only if try block fails")
else:
    print("I will run only if there is no exception. use this to nun code which should"
          "only exceute if there is no exception")
finally:
    print("This will be printed in every case")