# # # a = 10
# # # b = "abc"
# # # c = 29.0
# # # d = True
# # # print(a)
# # # print(b)
# # # print(c)
# # # print(d)
# # # print(type(a))
# # # print(type(b))
# # # print(type(c))
# # # print(type(d))
# # # l = ["a","b"]
# # # print(l)
# # # print(type(l)) 



# # # Arithmetic Operators
# # #-------------------------------      
# # # (Addition)        
# # # a = 10
# # # b = 9
# # # print(a+b)
# # # # (Sub)
# # # print(a-b)
# # # # (Mul)
# # # print(a*b)
# # # # (Div)
# # # print(a/b)
# # # # (Mod)
# # # print(a%b)
# # # # (Expo)
# # # print(a**b)
# # # # (Floor Div)
# # # c=1236
# # # d=10
# # # print(c//d)
# # #-------------------------------------------------------------------------------

# # # #Comparison Operators
# # # ---------------------------------------

# # # a = 10
# # # b = 4
# # # print(a==b)
# # # print(a!=b)
# # # print(a<b)
# # # print(a>b)
# # # print(a<=b)
# # # print(a<=b)

# # #-------------------------------------------------

# # #Assignment Operator
# # #---------------------------------------------------

# # # a = 10
# # #  print(a)
# # #  b=20
# # # a+=b
# # # print(a)
# # # a-=b
# # # print(a)
# # # a/=5
# # # print(a)
# # # a//=2
# # # print(a)
# # # a=20
# # # b=3
# # # a%=b
# # # print(a)
# # # a**=b
# # # print(a)

# # #--------------------------------------------------------------------

# # #Logical Operators
# # #-------------------------------------------------------------
# # a = False
# # b = True
# # print(a and b)
# # print(a or b)
# # print(not a)
# # print(not b)

# # b = False
# # a = True
# # print(a and b)
# # print(a or b)
# # print(not a)
# # print(not b)
# # #----------------------------------------------------------------------

# #membership operator
# #------------------------------------------------

# # a = "abcdef" 
# # print("y"in a)
# # print("b"in a)
# # print("c"not in a)
# # print("z" not in a)

# # x = [1,2,3,4,5]
# # print(3 in x)
# # print(6 not in x)
# # print(5 in x)
# # print(4 not in x)

# #----------------------------------------------------------------------------

# #Identity Operator
# #--------------------------------------

# # a = [1,2,3]
# # b = [1,2,3]
# # print(a is b)
# # # print(a is not b)
# # a=5
# # b=a
# # print(a is b)
# # # print(a is not b)
# # print(b is a)

# #---------------------------------------------------

# # Conditional Statement
# # -----------------------------------------
# # if
# # ----------------------
# # age = 17
# # if age>=20 :
# #     print('Eligible to vote')
#  #--------------------------------------

# #  if_else
# # -------------------------------------
# # age = 17
# # if age>=20 :
# #     print('Eligible to vote')
# # else :
# #     print("Not eligible")
# #----------------------------------------

# # mark = 51
# # if mark >50:
# #     print("Pass")
# # else :
# #     print("Fail")

# # a = 10
# # if a%2 == 0:
# #     print(a ,"is even")
# # else:
# #     print(a ,"is odd")

# # a = int(input("Enter a Number :"))
# # if a%2 == 0:
# #     print(a ,"is even")
# # else:
# #     print(a ,"is odd")

# # s = int(input("Enter Number :"))
# # if s > 0 :
# #     print(s,"Is Positive")
# # elif s < 0 :
# #     print(s,"Is Negative")
# # else:
# #     print("Is zero")

# # m = int(input("Enter Mark :"))
# # if m >=90 :
# #     print("A grade")
# # elif m>=80 :
# #     print("B grade")
# # elif m>=70 :
# #     print("C Grade")
# # elif m>=50:
# #     print("D grade")
# # else:
# #     print("Fail")

# #----------------------------------------------------------

# # #Nested if
# # --------------------------------

# # m = int(input("Enter Mark"))
# # if m > 50:
# #     if m>=90 :
# #         print("Grade A")
# #     elif m>=80 :
# #         print("Grade B")
# #     elif m>=70 :
# #         print("Grade C")
# #     else :
# #         print("Grade D")
# # else:
# #     print("Fail")

# #-------------------------------

# # n = int(input("Enter Number :"))
# # if n>0 :
# #     if n % 2 == 0:
# #         print(n,"Is even")
# #     else:
# #         print(n,"Is Odd")
# # elif n<0 :
# #     print(n,"Is Negative")
# # else :
# #     print("Number is zero")

# # -----------------------------------------------
# #1st prgm
# # ------------
# # s = int(input("Enter Salary :"))
# # n = int(input("Enter Year of Exp:"))
# # if n>5 :
# #     m=(s/100)*5
# #     s+=m
# #     print("Salary :",s)
# #     print("Bonus is :",m)
# # else :
# #     print("Salary :",s)
# #-----------------------------------

# #2nd prgm
# #------------
# # c = int(input("Enter Number of classes : "))
# # a = int(input("Enter Number of classes Attended: "))
# # p = (a/c)*100
# # print("Percentage : ",p)
# # if p>=75 :
# #     print("Allowed to Attend exan")
# # else :
# #     print("Not allowed to attend exam")
# # ------------------------------------------

# #3rd prgm
# #------------------

# # age = int(input("Enter Age : "))
# # s = input("Enter Gender : ")
# # m = input("Marital Status : ")
# # if s=="f" :
# #     print("Works at Urban Areas")
# # elif s=="m" :
# #     if age>20 and age<40 :
# #         print("Works Anywhere")
# #     elif age>40 and age<60 :
# #         print("Works at Urban Areas")
# #     else :
# #         print("ERROR")
# # ---------------------------------------    

# # a = int(input("Enter age of A :"))
# # b = int(input("Enter age of B :"))
# # c = int(input("Enter age of C :"))
# # if a>b and a>c:
# #     print("A is greater")
# #     if b>c :
# #         print("C is smallest")
# #     else:
# #         print("B is smallest")
# # elif b>c:
# #     print("B is greatest")
# #     if a>c :
# #         print("C is smallest")
# #     else:
# #         print("A is smallest")
# # else:
# #     print("C is greatest")
# #     if b>a :
# #         print("A is smallest")
# #     else:
# #         print("B is smallest")

# # n = int(input("Enter a Number"))
# # if n%2 == 0 and n%5 == 0 :
# #     print(n,"is divisible by both")
# # elif n%2 == 0:
# #     print("Divisible by 2")
# # elif n%5 ==0:
# #     print("Divisible by 5")
# # else:
# #     print("Not divisible")

# # n = int(input("Enter Number : "))
# # d1 = n%10
# # d2 = (n//10)%10
# # d3 = (n//100)%10
# # d4 = (n//1000)%10
# # rev = d1*1000+d2*100+d3*10+d4
# # print("Rev",rev)

# # a = int(input("Enter Number a: "))
# # b = int(input("Enter Number b: "))
# # print("Before Swap a=",a ," b =",b)
# # a,b = b,a
# # print("After Swap a=",a ," b =",b)

# # n = int(input("Enter Account Balance : "))
# # w = int(input("Withdrawal Amount : "))
# # if w <= n :
# #     if w%100 == 0 :
# #         print("Transaction Successful")
# #     else:
# #         print("Enter amount in multiples of 100")
# # else :
# #     print("Insufficient Balance")

# # s = int(input("Enter Salary :"))
# # c = int(input("Enter Credit Score :"))
# # l = int(input("Enter Loan Amount :"))
# # if s>=30000 :
# #     if c>=700 :
# #         if l <= 20*s :
# #             print("Loan Approved")
# #         else :
# #             print("Loan Amount is high")
# #     else:
# #         print("Improve Credit score")
# # else :
# #     print("Low Income")


# # n = input("Enter Food Type  : ")
# # if n == "veg" :
# #     print("Paneer :500, veg biriyani : 500")
# #     d = input("Enter Food  : ")
# #     q = int(input("Enter Quantity : "))
# #     if d == "paneer,veg" :
# #         b = 1000*q
# #     else :
# #         b = 500*q
# #     if b>=1000 :
# #         print("Bill = ",b, "Discount ",(b/100)*10)
# #     else:
# #         print("Bill = ",b, "No discount")

# # else :
# #      print("Chicken , Fish")
# #      d = input("Enter Food  : ")
# #      q = input("Enter Quantity : ")
# #     if d == "chicken,fish":
# #         m = 1000*q
# #     else :
# #         m = 500*q
# #     if m>=1000 :
# #         print("Bill = ",m, "Discount ",(m/100)*10)
# #     else:
# #         print("Bill = ",m, "No discount")

# # i = 1
# # while i<=10 :
# #     print("Number ",i) 
# #     i+=1

# # n = int(input("Enter Number : "))
# # i=1
# # while i<=n  :
# #     print(i)
# #     i+=1

#PASS STATEMENT --> BREAK  --> STOP THE LOOP
#---------------------------------

# # i = 0
# # while i<5 :
# #     print(i)
# #     if i == 3 :
# #         break
# #     i+=1
# # else:
# #     print("Loop Ended")


# i = 1
# while i<10 :
#     print(i)
#     if i==5 :
#         break
#     i+=1

# i=2
# while i<=20 :
#     print(i)
#     i+=2

# i=5
# while i<=50 :
#     print(i)
#     i+=5

# n = int(input("Enter Number : "))
# i=1
# while i <= n :
#     if i%2!=0:
#         print(i)
#     i+=1

#CONTINUE  --> SKIP THE ITERATION
#---------------------------
# i=1
# while i<10 :
#     if i==5 :
#         i+=1
#         continue
#     print(i)
#     i+=1
#----------------------------------

#PASS -->DO NOTHING
#------------------------------------

# i=1
# while i<5 :
#     if i==3 :
#         pass
#     print(i)
#     i+=1

#------------------------------------
#CUMILATIVE SUM
# ---------------------

# i = 1
# n = 0
# while i<=10 :
#     n=n+i
#     i+=1
# print("Sum is : ",n)

# i = 1
# s = 1
# while i<=10 :
#     s=s*i
#     i+=1
# print("Product : ",s)

# i = 1
# while i<=20 :
#     if i==10 :
#         i+=1
#         break
#     print(i)
#     i+=1

# -------------
# 2
# ------------------
# i = 1
# while i<=20 :
#     if i%2==0 :
#         i+=1
#         continue
#     print(i)
#     i+=1

#-----------------
# 3
# -----------
# i=1
# while i<=10 :
#     n=int(input("Enter a Number : "))
#     if n<0 :
#         print("Loop ended")
#         break
#     i=i+1
# -------------------------

# 4
# ---------------------------------
# i = 10
# while i>=0 :
#     print(i)
#     i-=1
#--------------------------------

# n = int(input("Enter Number : "))
# s=0
# i=1
# while i<=10 :
#     s=i*n
#     print(i,"*",n,"=",s)
#     i+=1

#--------------------------------------
#Prime Number :
#------------------------------

# i=1
# c=0
# n = int(input("Enter a Number : "))
# while i<n :
#     if n%i==0 :
#         c+=1
#     i+=1
# if c==2 :
#     print(n,"is Prime")
# else :
#     print(n,"is NOT Prime")

#-----------------------------------------------
#PALINDROME 
#-----------------------------------------

# n = int(input("Enter Number : "))
# t = n
# rev=0
# i=1
# while t > 0 :
#     rem=t%10
#     rev=rev*10+rem
#     t=t//10
# if rev == n :
#     print(n,"Is Palindrome")
# else :
#     print(n,"Is NOT Palindrome")

#=================================================

#FOR LOOP
#-------------------

# for digit in "123" :
#     print(digit)

# for i in range(5) :
#     print(i)

# for i in range(1,6,2):
#     print(i)

# -----------------------------
# PRINT EVEN NUMBERS
#------------------------------

# for i in range(2,11,2):
#     print(i)

# for i in range(1,11):
#     if i==5:
#         break
#     else:
#         print(i)
# else :
#     print("Loop ended")
# print("Helloo")


# for i in range(1,7):
#     if i==5:
#         continue
#     else:
#         print(i)
# else :
#     print("Loop ended")
# print("Helloo")

# Reverse a String  
# ---------------------

# s = input("Enter a string : ")
# rev=""
# for i in s :
#     rev=i+rev
# print(rev)
# if rev==s:
#     print("Palindrome")
# else :
#     print("Not Palindrome")

# -----------------------------------------

# Multiplication Table 
# -------------------------------
# n= int(input("Enter Number : "))
# s=0
# for i in range(1,11):
#     s=i*n
#     print(i,"*",n,"=",s)


# name = input("Enter employee name: ")
# department = input("Enter department: ")
# joining_date = input("Enter joining date: ")
# print("\n--- Welcome Message ---")
# print("Welcome to the company,", name)
# print("Your joining date is", joining_date)
# print("\n--- Onboarding Instructions ---")
# print("1. Complete employee registration.")
# print("2. Collect your ID card.")
# print("3. Meet the HR representative.")
# print("4. Attend the orientation session.")
#-----------------------------------------------

#No of digits
#------------------------------
# n = int(input("Enter Number : "))
# t=n
# c=0
# while t > 0 :
#     rem=t%10
#     c+=1
#     t=t//10
# print("No of digit : ",c)
# #---------------------------------

#sum of digits
#---------------------------------
# n = int(input("Enter Number : "))
# t=n
# s=0
# while t > 0 :
#     rem=t%10
#     s+=rem
#     t=t//10
# print("Sum is : ",s)
#-------------------------------------

# n = int(input("Enter Number : "))
# t=n
# p=1
# while t > 0 :
#     rem=t%10
#     p*=rem
#     t=t//10
# print("Product is : ",p)
#---------------------------------------

# armstrong
# ---------------------

# n = int(input("Enter Number : "))
# t=n
# c=0
# while t > 0 :
#     c+=1
#     t=t//10
# print("No of digit : ",c)
# t=n
# rev=0
# while t > 0 :
#     rem=t%10
#     rev=rev+rem**c
#     t=t//10
# if rev==n:
#     print(" Armstrong : ",rev)
# else:
#     print("Not Armstrong ",rev)

#prime using for
#-----------------------------

# n = int(input("Enter Number : "))
# c = 0
# t=n
# for i in range(1,n+1):
#     if  t%i == 0 :
#         c+=1
# if c==2 :
#     print(t,"is Prime ")
# else:
#     print(t,"is NOT Prime ")

#Even Numbers Between limits
#-----------------------------------
# n = int(input("Enter starting limit : "))
# e = int(input("Enter ending limit : "))
# for i in range(n,e,2):                    
#     print("Numbers are : ",i)
# ---------------------------------------------

#  #String Reversal
# --------------------------
# n = ""
# s = input("Enter String : ")
# for i in s :
#     n=i+n
# print("Reve is : ",n)
# if s==n :
#     print("Palindrome ")
# else :
#     print("NOT Palindrome ")

# -----------------------------------------------

#Fibinocci
#--------------------

# l = int(input("Enter Limit : "))
# n=0
# m=1
# print(n,m)

# for i in range(1,l-1):
#     s=n+m
#     print(s)
#     n=m
#     m=s
#-------------------------------------    

#NESTED For
#----------------------------------

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#-------------------------------------

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

# STRING OPERATION
# ----------------------------

# CONCATENATION
# ------------------------

# n = input("Enter : ")
# s = input("Enter : ")
# print(n+s)
# ----------------------------

# REPETITION
# ------------------------

# n = input("Enter : ")
# print(n*3)
# ------------------------

# Membership operator
# -------------------------
# n = input("Enter : ")
# print("h" not in n)
# print("w"  in n)
# ------------------------------


#Positive Indexing
# ----------------------------

# s = input("Enter : ")
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(len(s)) 

#Negative Indexing
# ----------------------------
# s = input("Enter : ")
# print(s[-1])
# print(s[-2])
# print(s[-3])

#String Slicing
#----------------------
# s = "abcdefghi"
# print(s[0:5:2])
# print(s[1:5])
# print(s[:5])
# print(s[5:])
# print(s[:5]+s[5:])

#NEGATIVE SLICING
#--------------
# s="datascience"
# print(s[::-1]) #reverse
# print(s[5:0:-1])
# print(s[-1::-1])
#---------------------------------


# s = "Programming in python"
# print(s[:5])
# print(s[-4::])
# print(s[1:-1])
# print(s[1::2])
# print(s[::2])
# print(s[::-1])


# s = input("Enter String : ")
# print(s[0],s[-1])

#PATTERN PRINTING
#---------------------------
# for i in range(1,6) :
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()
#------------------------------------
# for i in range(5,0,-1) :
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()
#----------------------------------------

# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()
#--------------------------------------

# for i in range(5):
#     for j in range(i+1):
#         print(2*i,end=" ")
#     print()

#--------------------------------------------

# for i in range(1,6):
#     for j in range(i):
#         if i%2==0:
#             print(2,end=" ")
#         else :
#             print(1,end=" ")
#     print()
#-----------------------------------------------

# for i in range(1,6) :
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# -----------------------------------------------

# for i in range(6,1,-1) :
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#------------------------------------------------------

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()
#-----------------------------------------------------
# for i in range(5,0,-1):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#------------------------------------------------

# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print()
# for i in range(6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# -------------------------------------------------


# s = input("Enter String : ")
# print(s[0],s[-1])

# l=len(s)
# print(s[l//2])

# print(s[::-1])

# rev=s[::-1]

# if rev==s:
#     print("Palindrome ")
# else :
#     print("NOT palindrome")

# c=0
# for i in s :
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
#         c+=1
# print("Count of vowels : ",c)

# a=""
# for i in range(0,len(s),2) :
#     a+=s[i]
# print(a[::-1])
 
# c=0
# l=len(s)
# for i in range(l):
#     if s[i] ==" " :
#         c+=1
# print("no of spaces : ",c)

# if s == "" :
#     print("Empty ")
# else :
#     print("Not Empty")

# n=len(s)
# print("First half :",s[0:n//2])
# print("First half :",s[n//2:n])

# print(s[1:-1])
# -----------------------------

#  STRING METHODS
# -------------------------

#CASE CONVERSION METHODS
#--------------------------------

# s = "data sCIENCE"
# print(s.upper())
# print(s.lower())
# print(s.capitalize()) #first letter of sentence
# print(s.title()) #first letter of each word
# print(s.swapcase())#swap low to up & up to lower
# print(s.casefold()) #beta characters

#VALIDATION METHODS
#-------------------------

# s = "Data Science"
# n = "SCIENCE"
# f = "data 125"
# l = "   "
# m="15.2"
# print(n.isupper())
# print(n.islower())
# print(s.istitle())
# print(s.isalpha())#if all the char are alphabets
# print(n.isalpha())
# print(f.isalnum())#if char is alpha and num
# print(l.isspace())
# print(m.isdigit())#number combinations ,fractions
# print(m.isdecimal())#only numbers
# print(m.isnumeric())
#-------------------------------------------

#Search and Find Functions
#-------------------------------
s="welcome hai"
# print(s.find("z")) #return index
# print(s.index("l")) #return index if not found error message
# print(s.rfind("l")) #search from right
# print(s.rindex("o")) #search from right if not found error message
#count
#----------
# print(s.count("l"))  #occurence of character

#startswith
#---------------------
# print(s.startswith("wel")) #checks the starting
# print(s.startswith("Wel"))
# print(s.startswith("wel",0))#startswith(value,start index,end index)
# print(s.startswith("welc",8,5)) #checks the starting


#endswith
#------------------------
# print(s.endswith("hai")) #checks the ending
# print(s.endswith("Hai"))
# print(s.endswith("hai",8))#endswith(value,start index,end index)
# print(s.endswith("hai",8,11)) #checks the ending
#------------------------------------------------------------------------


#4) Modification/Replace functions
#-----------------------------------------

#replace()
# s = "hello"
# n = s.replace("l","z")
# print(s)
# print(n)

#strip() - remove space from sentences  from starting or ending
# s = "  hello    "
# print(s.strip())
# print(s.lstrip()) #-remove space from left
# print(s.rstrip()) #-remove space from right

#split() - split sentence  [split(seperator,maxsplit)]
# s = "data analystics"
# print(s.split(" "))
# print(s.split("a"))
# print(s.split("a",3))

# #rsplit()-split from right
# print(s.rsplit("a",2))
# print(s.rsplit("t",2))


#join() - [ seperator.join(iteration) ]-for join strings in list
# l = ["apple","banana","orange"]
# print(" ".join(l))
# print("-".join(l))

#ALIGNMENT FUNCTION
# ---------------------------

# ljust() -align to left and fill characters based on width [string.ljust(width,fillchar)]
# s="python"
# print(s.ljust(12,"s"))

# rjust() -align to right and fill characters based on width [string.ljust(width,fillchar)]
# s="python"
# print(s.rjust(12,"*"))

#center() - center align
#-------------------------------
# s="python"
# print(s.center(12,"*"))

#zfill() - zero padding
#-----------------------------
# s = "55"
# print(s.zfill(10))
# print(s.zfill(6))

#---------------------------------

# s="python"
# print(dir(s)) #print directories of functions

#-------------------------------

#isascii() - return boolean if it has ascii value 
# s = "hgh"
# a = "abc"
# print(s.isascii())
# print(a.isascii())
# print(s.isidentifier())

#--------------------------------------

#isprintable() - if the character is printable
#---------------------------------------------
# s="bhghghjg"
# s="ahbhbhuyu\n"
# print(s.isprintable())
# print(a.isprintable())
#[escape characters : /n,/t]
#--------------------------------------

















