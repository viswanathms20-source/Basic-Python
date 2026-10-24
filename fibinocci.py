
l = int(input("Enter Limit : "))
n=0
m=1
print(n,m)
s=n+m
for i in range(1,l-1):
    print(s)
    n=m
    m=s
    s=n+m