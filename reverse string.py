
s = input("Enter a string : ")
rev=""
for i in s :
    rev=i+rev
print(rev)
if rev==s:
    print("Palindrome")
else :
    print("Not Palindrome")
