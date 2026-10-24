i=1
c=0
n = int(input("Enter a Number : "))
while i<n :
    if n%i==0 :
        c+=1
    i+=1
if c==2 :
    print(n,"is Prime")
else :
    print(n,"is NOT Prime")