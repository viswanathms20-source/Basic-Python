# def hello():
#     print("hello world")
# hello()

# def sum(a,b):
#     print(a+b)
# sum(4,5)
# sum("hello ","world")

# def display(name,course):
#     print(name ,"is studying ",course)
# n=input("Enter Name : ")
# c=input("Enter Course : ")
# display(n,c)

# def display(name,course="da"):          #set default value for parameter
#     print(name ,"is studying ",course)
# n=input("Enter Name : ")
# c=input("Enter Course : ")
# display(n,c)
# display(n)

# def add(a,b):           #return an value
#     return a+b
# result=add(5,10)
# print(result)

#types of arguments
#--------------------------

#positional argument
#------------------
# def sub(a,b):   #pass arguments according to the match or position
#     print(a-b)
# sub(10,5)
# sub(5,10)

#arbitrary argument   #varibale length /multiple element
#------------------
# def display(*a):   #allows us to pass any no. of positional arguments
#     print(a)
#     print(type(a))
# display(1,2,3,4,5)    #return a tuple

# def add(*num):
#     print(sum(num))
# add(1,2,3,4,5,6)

#keyword arguments     #we can specify parameter names while calling the functions
#--------------------

# def display(a,b,c):
#     print(a,b,c)
# display(a=10,c=5,b=4)

#arbitrary keyword argument   
#--------------------------
# def display(**x):
#     print(x)
#     print(type(x))
# display(a=10,c=23,b=3)  #return a dictionary
#--------------------------------------------------------


#returning multiple values
# def cal(a,b):
#     sum=a+b
#     diff=a-b
#     return sum,diff
# s,d=cal(10,20)
# print("Sum is :",s)
# print("Diff is : ",d)

# def student():
#     name=input("Enter name : ")
#     age=int(input("Enter Age : "))
#     cource=input("Enter Course : ")
#     return name,age,cource
# n,a,c=student()
# print("Name is ",n,"Age ",a,"Course ",c)


# def large(a,b):
#     if a>b :
#         return a
#     else :
#         return b
# n1=int(input("Enter First Number : "))
# n2=int(input("Enter Second Number : "))
# print("Largest is ",max(n1,n2))


# def vowels(s):   #vowels
#     v="aeiou"
#     c=0
#     for i in s: 
#         if i in v:
#             c+=1
#     return c
# s=input("Enter String : ")
# print("No of vowels : ",vowels(s))

# def oddeven(n):   #odd even
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("Enter number : "))
# print(n ,"is ",oddeven(n))

# def rev(s):   #reverse a string
#     char=""
#     for i in s:
#         char=i+char
#     return char
# s=input("Enter String : ")
# print("reverse is :",rev(s))

# def rev(s):   #reverse a string
#     return s[::-1]
# s=input("Enter String : ")
# print("reverse is :",rev(s))


# def add(n):    #sum of list
#     return sum(n)
# l=[]
# n=int(input("Enter limit :"))
# for i in range(n):
#     user=int(input("Enter Element : "))
#     l.append(user)
# print("Sum is : ",add(l))
#-------------------------------------------------------

#Local Variable
#----------------------------------
# def display():
#     x=10
#     print(x)
# display()
# print(x)   #cause an error because "x" is n local variable

#Global Variable
#----------------------------------
# x=10  #"x" is defined as global
# def display():
#     print(x)
# display()
# print(x)


# x=10   #"x" is defined as local and global
# def display():
#     x=50
#     print(x)
# display()
# print(x)

# x=10   
# def display():
#     global x
#     x=50
#     print(x)
# display()
# print(x)
# print(x)

#-------------------------------------------------------------------------
#PASS BY VALUE: when a  copy of the varible is passed to the function, 
# changes made to the varibale inside the function do not affect the 
# original variable outside the funcion
#-------------------------------------------------------------------------
# def modify(x):
#     x=x+5
#     print("inside fn",x)
# x=10
# modify(x)
# print("outside fn ",x)

#-------------------------------------------------------------------------
#PASS BY REFERENCE: when a  reference of the varible is passed to the function, 
# changes made to the varibale inside the function affect the 
# original variable outside the funcion
#-------------------------------------------------------------------------
# def modify(l):
#     l.append(10)
#     print("inside fn",l)
# l=[1,2,3]
# modify(l)
# print("outside fn ",l)
#------------------------------------------------------------------------------

#RESURSION
#-------------------------
# def display(x):
#     if x==0:
#         return x
#     else:
#         return x+display(x-1)
# n=int(input("Enter Number : "))
# print("Cumulative sum ",display(n))

#FACTORIAL
#-------------
# def fact(x):
#     if x==1 or x==0:
#         return 1
#     else :
#         return x*fact(x-1)
# n=int(input("Enter Number : "))
# print("Factorial  : ",fact(n))

# def display(x):
#     if x==0 :
#         return 0
#     else:
#         print(x)
#         display(x-1) 
# n=int(input("Enter Number : "))
# display(n)

#--------------------------------------------------------

#-------------------------------------------------------

#LAMBDA FUNCTIONS
#-------------------
# lambda fn is mainly used when we need a short 
# functiom just once
# can give any no. of arguments, but a single expression 
# dont have to specify a fn name(anonymous)

#lambda arguments: expresiion

# #square of number 
# x=lambda a:a**2
# n=int(input("Enter Numbers : "))
# print(x(n))



