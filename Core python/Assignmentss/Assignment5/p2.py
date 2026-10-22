#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

n = int(input("Enter number of Students:"))
total = 0
total_percentage = 0

for i in range(n):
    maths = int(input("Enter math marks:"))
    english = int(input("Enter marks of english:"))
    geogrphy = int(input("Enter marks of geography:"))
    java = int(input("Enter marks of java:"))
    dbms = int(input("Enter marks of dbms:"))
    total = maths + english + geogrphy +java +dbms

    percentage = total / 5
    print('Percentage=',percentage)

    total_percentage += percentage
average = total_percentage/n
print('Average percentage:',average)
