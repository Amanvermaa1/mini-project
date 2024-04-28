name = input("Enter your name: ")
sub = int(input("No of Subjects: "))
marks = []
for i in range(sub):
    sub_name=input("Enter subject name:")
    sub_mark = float(input(f"Enter marks for subject {i+1}: {sub_name} : "))
    marks.append(sub_mark)

total_marks = sub*100
get_marks = sum(marks)
per = (get_marks / total_marks) * 100

print("\n")
print("Name:", name)
print("Total Marks:", total_marks)
print("You Got :",get_marks)
print(f"per: {'%.2f' % per}%")

if per >= 33:
    if per == 100 :
        grade = 'O'
    elif per >= 90:
        grade = 'A+'
    elif per >= 80:
        grade = 'A'
    elif per >= 70:
        grade = 'B+'
    elif per >= 60:
        grade = 'B'
    elif per >= 50:
        grade = 'C'
    elif per >= 40:
        grade = 'D'
    else:
        grade = 'E' 
else:
    grade = 'F'
    
print("Grade:", grade)
if grade != 'F':
    result = 'PASS'
else :
    result = 'FAIL'
print("Result : ",result)