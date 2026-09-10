#Print 1 to 10

# i = 1

# while i <= 10:
#     print(i)
#     i += 1


#Print 10 to 1

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1


#Even Numbers

# i = 2

# while i <= 20:
#     print(i)
#     i += 2


#Sum 1 to 10

# i = 1 

# total = 0

# while i <= 10:
#     total = total + i
    
#     i += 1
    
# print(total)

#Count from 1 to 10 using a while loop.

# i = 1

# count = 0

# while i <= 10:
#     count = count + 1
#     i += 1
    
# print(count)

#Stop at 5

#i = 1

# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1


#Skip 5

# i = 1

# while i <= 10:
#     if i == 5:
#         i = i + 1
#         continue
    
#     print(i)
#     i += 1


#Password


# password = ""

# while password != "Likith@2006":
#     password = input("Enter the number:")
    
    
# print("login succesfull")


#Number Guessing

# secret = 7


# number = int(input("Enter the number:"))

# while number != secret:
#      print("Wrong number")
#      number = int(input("Enter the number:"))
    
    
# print("Gussed Correct")





#AI/ML Data Processing

# data = [10, 20, -1, 30, -1, 40, 50]

# i = 0

# while i < len(data):
#     if data[i] == -1:
#         i += 1
#         continue
#     print(data[i])
#     i += 1



#Second Highest Number

# numbers = [45, 89, 23, 100, 67, 92, 100, 78]

# first_highest = numbers[0]
# second_highest = numbers[0]

# for num in numbers:
#     if num > first_highest:
#         second_highest = first_highest
#         first_highest = num
        
#     elif num > second_highest and num != first_highest:
#         second_highest = num
        
# print("First highest:",first_highest)
# print("Second highest:",second_highest)


#Second Lowest Number

# numbers = [45, 12, 67, 23, 89, 12, 34, 56]

# first_lowest = numbers[0]
# second_lowest = numbers[0]

# for num in numbers:
#     if num < first_lowest:
#         second_lowest = first_lowest
#         first_lowest = num
    
#     elif num < second_lowest and num != first_lowest:
#         second_lowest = num
        
        
# print(second_lowest)


#Separate Even and Odd


# numbers = [12, 45, 67, 22, 90, 33, 18, 51, 76]

# even =[]
# odd = []


# for num in numbers:
#     if num %2 == 0:
#         even.append(num)
    
#     else :
#         odd.append(num)
        
# print(even)
# print(odd)



#Duplicate Finder

# numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

# check = []
# Duplicate = []

# for num in numbers:
#     if num in check:
#         if num not in Duplicate:
#             Duplicate.append(num)
            
#     else:
#         check.append(num)
            
# print("Duplicates are:",Duplicate)


#Remove Duplicates Without

# numbers = [10, 20, 30, 20, 40, 10, 50, 30, ]

# check = []
# remove = []

# for num in numbers:
#     if num in check:
#         if num not in remove:
#             remove.append(num)
            
#     else:
#         check.append(num)
        
# print(check)


#Frequency Counter

# numbers = [10, 20, 10, 30, 20, 10, 40]

# frequency = {}

# for num in numbers:
#     if num in frequency:
#         frequency[num] = frequency[num] + 1
        
#     else:
#         frequency[num] = 1
    
# print(frequency)


#Find Missing Number

# numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

# missing = []

# for num in range(1,11):
#     if num not in numbers:
#         missing.append(num)
        
# print(missing)


#Consecutive Numbers

# numbers = [10, 11, 12, 15, 16, 20, 21, 22]

# first = []
# second = []
# third = []

# for num in numbers:
#     if num < 15:
#         first.append(num)
#     elif num < 20:
#         second.append(num)   
#     else:
#         third.append(num)
        

# print(first,second,third)


#Reverse a List Without

# numbers = [10, 20, 30, 40, 50]

# reverse = []

# for i in numbers:
#     reverse.insert(0,i)
    
# print(reverse)


#Find Common Elements


# a = [10, 20, 30, 40, 50]
# b = [30, 40, 50, 60, 70]



# for num_a in a:
#     for num_b in b:
#         if num_a == num_b:
#             print(num_a)


#Digit Counter

# number = int(input("Enter the number:"))

# count = 0
# while number > 0:
#     number = number // 10
#     count += 1
    
    
# print(count)




#Reverse a Number


# number = int(input("Enter the number:"))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
    
# print(reverse)


#Sum of Digits



# number = int(input("Enter the number:"))

# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10
    
# print(total)


#Palindrome Number

# number = int(input("Enter the number:"))

# original = number
# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
    
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




#Armstrong Number


# number = int(input("Enter the number:"))

# original = number
# total = 0

# while number > 0:
#      digit = number % 10
#      total = total + digit ** 3
#      number = number // 10
    
# if total == original:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong number")  


#Number Guessing

# secret = 73

# number = int(input("Enter the number:"))

# while secret != number:
#     print("Wrong answer:")
    
#     number = int(input("Enter the number:"))

# print("Gussed Correct")
    
    
    
    
    
    
    
    
#Student Data Analysis

# marks = [78, 92, 45, 33, 87, 29, 95, 61, 72, 88]

# total = 0
# highest = marks[0]
# lowest = marks[0]
# count = 0
# fail = 0
# score = 0
# Total = 0

# for num in marks:
#     total = total + num
# print("Total marks is:",total)

# for num in marks:
#     average = total/10
# print("Average is :",average)

# for num in marks:
#     if num > highest:
#         highest = num
# print("Highest marks is:",highest)

# for num in marks:
#     if num < lowest:
#         lowest = num
# print("Lowest marks is:",lowest)

# for num in marks:
#     if num >= 35:
#         count = count + 1
# print("Students passed:",count)

# for num in marks:
#     if num <= 35:
#         fail = fail + 1
# print("Students failed:",fail)

# for num in marks:
#     if num >= 80:
#         score = score + 1
# print("Greater than 80:",score)


# for num in marks:
#     if num >= 80:
#         Total = Total + 1
        
# print("Total is :",Total)



#Data Cleaning & Filtering


data = [10, -1, 25, 50, 0, 75, -1, 90, 35, 100, -5]

count = 0
total = 0
highest = data[0]
lowest = data[0]
Count = 0


for num in data:
    if num < 0:
        data.remove(num)
print("Vaild values are:",data)

for num in data:
    if num > 0:
        count = count + 1
    
print("Count of Valid numbers:",count)

for num in data:
    if num > 0:
        total = total + num
print("Total number is :",total)

for num in data:
    if num > highest:
        highest = num
print("Highest number is:",highest)

for num in data:
    if num < lowest:
        lowest = num
        
print("Lowest values is:",lowest)

for num in data:
    if num < 50:
        Count = Count + 1
        
print("Greater Than 50:",Count)
        
    

        











    








        

    
    
    

    
    
    
        

        

