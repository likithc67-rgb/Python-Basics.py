#3 × 3 Stars

# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()
        
        
        
#4 × 5 Rectangle


# for i in range(4):
#     for j in range(5):
#         print("*", end=" ")
#     print()


#Number Pattern

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()


# Number Pattern

# for i in range(1,4):
#     print(i)


# Square Number Pattern

# for i in range(1,4):
#      for j in range(1,4):
#          print(i,end=" ")
#      print()


# Increasing Pattern

# for i in range(1,5):
#     for j in range(1,i + 1):
#         print(j,end=" ")
#     print()



#Multiplication Tables

# for i in range(1,11):
#     for j in range(1,3):
#         print(i * j,end=" ")
#     print()


#Star Triangle

# for i in range(1,5):
#     for j in range(1,i + 1):
#         print("*",end=" ")
#     print()


#Reverse Triangle

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# #Mini Challenge

# data = [
#      [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90]
#  ]

# for i in data:
#     for j in i:
#         print(j)


#=======BREAK AND COUNTINUE===========


#Stop at 5


# for j in range(1,6):
#         if j == 5:
#             break
#         print(j,end=" ")
# print()


# Skip 5


# for i in range(1,6):
#     if i == 3:
#         continue
# print(i)


#Find Number

# numbers = [10, 20, 30, 40, 50]

# # for num in numbers:
# #     if num == 30:
# #         print("The number Found",num)
# #         break


#Skip Odd Numbers

# numbers = [10, 15, 22, 33, 40, 51, 60]

# for num in numbers:
#     if num %2 == 0:
#         print(num)
#         continue


#Stop at Negative Number


# numbers = [10, 20, 30, -5, 40, 50]

# for num in numbers:
#     if num <= 0:
#         print("Negative number Found:",num)
#         break


#Skip Failed Students


# marks = [78, 32, 65, 29, 91, 45, 20]

# for mark in marks:
#     if mark < 35:
#         print(mark)
#         continue


#Search Student

# students = ["Rahul", "Likith", "Arun", "Kiran", "Ravi"]

# for name in students:
#     if name == "Likith":
#         print("Found your name:",name)
#         break


#First Number Greater Than 50


# numbers = [10, 25, 45, 67, 80, 90]

# for num in numbers:
#     if num > 50:
#         print("The number is found:",num)
#         break


#Skip Multiples of 3

for i in range(1,21):
    if i % 3 == 0:
        continue
   
    print(i)


#AI/ML Data Cleaning



# data = [10, 20, -1, 30, -1, 40, 50]

# for num in data:
#     if num <= 0:
#         continue
#     print(num)
       
    


    