n = int(input("Enter Number : "))
t=n
c=0
while t > 0 :
    c+=1
    t=t//10
print("No of digit : ",c)
t=n
s=0
while t > 0 :
    rem=t%10
    s=s+rem**c
    t=t//10
if rev==n:
    print(" Armstrong : ",rev)
else:
    print("Not Armstrong ",rev)
