# Enumerate

#========== Normal Ways ===============

a = ["CodeWithHarry", "T Series", "Mixer Grinder", "Pen"]

# i = 0
# for item in a:
#     i = i + 1
#     if i%2 == 0:
#         print(item)

# for i, item in enumerate(a):
#         print(i, item)

#====== Output ======
    # 0 CodeWithHarry
    # 1 T Series
    # 2 Mixer Grinder
    # 3 Pen

for i, item in enumerate(a):
    if (i + 1)%2 == 0:
        print(i, item)

