#PATTERN PRINTING
#-----------------------------

# for i in range(1,5):
#     for j in range(1,5):
#         print(i, end="")
#     print()


# for i in range(1,5) :
#     for j in range(1,5):
#         print(j,end="")
#     print("")


# for i in range(1,5) :
#     for j in range(1,5):
#         print("*",end="")
#     print("")


# for i in range(1,5):
#     for j in range(0,i):
#         print("*",end="")
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
#------------------------------------------


# for i in range(1,6) :
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1) :
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1) :
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()

#-----------------------------------
# for i in range(5):
#     for j in range(i+1):
#         print(2*i,end=" ")
#     print()
#---------------------------------------

# for i in range(1,6):
#     for j in range(i):
#         if i%2==0:
#             print(2,end=" ")
#         else :
#             print(1,end=" ")
#     print()
# -----------------------------------------
for i in range(6) :
    for j in range(i):
        print(j,end=" ")
    print()
# ---------------------------------------
# for i in range(6,1,-1) :
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
# -------------------------------------
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
#----------------------------------------
# for i in range(5,0,-1):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#--------------------------------------
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
print()
for i in range(6):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()





