# #Q1. Employee Details

# Employe_name = "Likith"
# Employe_id = 114
# Age = 21
# Department = "Softeware"
# Salary = 75000

# print("Employe name:",Employe_name,type(Employe_name))
# print("Employe id:",Employe_id,type(Employe_id))
# print("Age",Age,type(Age))
# print("Department:",Department,type(Department))
# print("Salary:",Salary,type(Salary))

#Q2. Simple Calculator

# a = 25
# b = 10

# print("Addition = ", a + b)
# print("Subtraction = ", a - b)
# print("Multiplication = ", a * b)
# print("Division = ", a / b)
# print("Floor Division = ", a // b)
# print("Reminder = ", a % b)

# #Q3. Temperature Conversion

# celsius = 35

# Fahrenheit =  (celsius * 9/5) + 32

# print("Temperature is :",Fahrenheit)

# #Q4. Rectangle

# length = 20
# width = 12

# print("Area of Rectangle is:",length * width)
# print("Perimeter of Rectangle is:", 2 * (length+width))

#Q5. Circle

# r = 7

# print("Area of a circle is:", 3.14 * r ** 2)
# print("Circumference of a circle is :", 2 * 3.14 * r)

#Q6. Shopping Cart

# price = "250"
# quantity = "4"
# discount = "50"

# price = int(price)
# quantity = int(quantity)
# discount = int(discount)

# total = price * quantity
# after_discount = total - discount

# print("The total bill is:",total)
# print("After the discount the bill is:",after_discount)

# #Q7. Student Marks

# maths = "85"
# physics = "78"
# python = "92"

# maths = int(maths)
# physics = int(physics)
# python = int(python)

# Total = maths + python + physics
# Average = Total / 3

# print("The Total marks is :",Total)
# print("The Average marks is :",Average)

#Q8. Age Calculator

# birth_year = "2005"
# current_year = 2026

# birth_year = int(birth_year)

# calculate = current_year - birth_year

# print("Your age is :",calculate)

#Q9. Subject List

# Subject = ["Maths","Python","Java","Chemistry","Biology"]

# print("The list of Subject cointains:",Subject)
# print("The first subject of the list is:",Subject[0])
# print("The last subject of the list is:",Subject[4])
# Subject.append("Kannada")
# print("Add the subject Kannada:",Subject)
# Subject.remove("Java")
# print("The removed subject from the list is:",Subject)
# print("The length of the list is:",len(Subject))

#Q10. Marks List

# marks = [78, 88, 67, 91, 84]

# print("The total marks is:",sum(marks))
# print("The average marks is:",sum(marks) / len(marks))

# highist = marks[0]
# lowest = marks[0]

# for mark in marks:
#     if mark > highist:
#        highist = mark
#     if mark < lowest:
#         lowest = mark
# print("The highest marks is :",highist)
# print("The lowest marks is :",lowest)
# print("The length of the list:",len(marks))

#Q11 — Tuple Create a tuple

# subject = ("Python","Java","C","C++","Javascript")

# print("The Tuple is:",subject)
# print("The first item of the tuple is:",subject[0])
# print("The last item of the tuple is:",subject[-1])
# print("The number of item in the tuple is :",len(subject))

# subject = ("Pandas",) + subject[1:]

# print("The new first item of the tuple is:",subject)



#Q12 — Tuple Operations


# languages = ("Python", "Java", "C", "Python", "Java")

# print("How many times python occurs:",languages.count("Python"))
# print("The position of the java in which index",languages.index("Java"))
# print("The length of the tuple is :",len(languages))


#Q13 — Remove Duplicates


# numbers = [10, 20, 30, 20, 40, 10, 50, 30]

# unique_number = []

# for num in numbers:
#     if num not in unique_number:
#         unique_number.append(num)

# print("The unique values are:",unique_number)


#Q14 — Common Numbers

# a = {10, 20, 30, 40, 50}
# b = {30, 40, 50, 60, 70}

# both_sides = []

# for num in a:
#     if num in b:
#         both_sides.append(num)
# print("The common number from a and b is :",both_sides)
# print("The numbers present in a is :", a)
# print("The numbers present in b is:",b)
    

#Q15 — Student Dictionary

# student = {
#     "name": "Likith",
#     "age": 20,
#     "course": "CSE",
#     "marks": 84
# }


# print("Name:",student["name"])
# print("Cource is:",student["course"])
# student["marks"] = 88
# print("The new marks of the student is:",student)
# student["city"] = "Banglore"
# print("The city name is:",student)
# student.pop("city")
# print("The removed city is:",student)
# print("The new details is:",student)


#Q16 — Employee Salary

# employee = {
#     "name": "Rahul",
#     "basic": 25000,
#     "hra": 5000,
#     "da": 3000
# }

# salary = employee["basic"]+employee["hra"]+employee["da"]

# print("The salary of the rahul is:",salary)

#Q17 — Student Marks

# marks = {
#     "Maths": 78,
#     "Physics": 87,
#     "Chemistry": 82,
#     "Python": 91,
#     "DBMS": 85
# }

# total = marks["Chemistry"] + marks["Maths"] + marks["DBMS"] + marks["Physics"] + marks["Python"]
# average = total / len(marks)

# highest = marks["Maths"]
# lowest = marks["Maths"]

# for key in ["Chemistry","DBMS","Maths","Physics","Python"]:
#     if marks[key] > highest:
#         highest = marks[key]
#     if marks[key] < lowest:
#         lowest = marks[key]
    
# print("The total marks of the student is:",total)
# print("The average marks of the student is:",average)
# print("The highest marks of the student is:",highest)
# print("The lowest marks of the student is:",lowest)

#Q19 — Student Result


# maths = 78
# physics = 65
# chemistry = 81
# python = 92
# dbms = 55

# total = maths + physics + chemistry + python + dbms
# average = total / 5
# Percentage = (total/500) * 100

# print("The total marks of the student is:",total)
# print("The average marks of the student is:",average)
# print("The percentage of the student is",Percentage,"%")



# if maths >= 35 and physics >= 35 and chemistry >= 35 and python >= 35 and dbms >= 35:
#     print("The student is Passed")
# else:
#     print("The student is Failed")



#Q20 — Mini Student Profile Project

# Create a small Student Profile Program.


# print("===== STUDENT PROFILE =====")

# Name = "Likith c Kanth"
# Age = 20
# USN = "4Al24CS114"
# Course = "CSE"
# maths = 78
# physics = 65
# chemistry = 81
# python = 92
# dbms = 55

# print("Name:",Name)
# print("Age:",Age)
# print("USN:",USN)
# print("Cource:",Course)

# print("maths:",maths)
# print("Physics:",physics)
# print("Chemisrty:",chemistry)
# print("Python:",python)
# print("DBMS:",dbms)

# total = maths + physics + chemistry + python + dbms
# average = total / 5
# percentage = (total / 500) * 100

# print("Total:",total)
# print("Average:",average)
# print("Percentage:",percentage)

# if maths >= 35 and physics >= 35 and chemistry >= 35 and python >= 35 and dbms >= 35:
#     print("Result:Passed")
# else:
#     print("The student is Failed")