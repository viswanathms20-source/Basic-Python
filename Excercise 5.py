def total(m):
    return sum(m)

def percentage(t,s):
    return t//s

def grade(p):
    if p > 90 :
        return "A"
    elif p > 80 :
        return "B" 
    elif p > 70 :
        return "C"
    elif p > 60 :
        return "D"
    else :
        return "F"

def result_status(marks):
    l=[]
    for i in marks:
        if i <= 35 :
            l.append("Fail")
        else :
            l.append("Pass")
    return l

def report_card(name,sub,marks,total,percentage,grade,status):
    print("\n----- STUDENT REPORT CARD -----")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage,"%")
    print("Grade:", grade)
    print("---Result Status---")
    print("Subject--Mark--Grade")
    for i in range(len(marks)):
        print(sub[i],marks[i],status[i])

n=input("Enter Name : ")
s=["Malayalam","Hindi","Maths","English","Chemistry"]
marks=[]
for i in s:
    print("Enter Marks of ",i,end=" ")
    m=int(input(": "))
    marks.append(m)
print(marks)
t=total(marks)
per=percentage(t,5)
g=grade(per)
status=result_status(marks)
report_card(n,s,marks,t,per,g,status)