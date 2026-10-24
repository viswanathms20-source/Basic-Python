
n = int(input("Enter Number : "))
t = n
rev=0
i=1
while t > 0 :
    rem=t%10
    rev=rev*10+rem
    t=t//10
if rev == n :
    print(n,"Is Palindrome")
else :
    print(n,"Is NOT Palindrome")
