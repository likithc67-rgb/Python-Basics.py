# def welcome():
#     print("Hello! Welcome to Python")
    
# welcome()
# welcome()
# welcome()


# def student(name, age, branch):
#     print("Name:",name)
#     print("Age:",age)
#     print("Brsnch",branch)
    
# student("Likith",20,"CSE")


# def calculate_area(length, width):
#     area = length * width
#     return area

# ans = calculate_area(5,10)
# print("Area", ans)

# def check_age(age):
#     if age > 18:
#         print("You are eligible")
#     else:
#         print("You are not eligible")
        
# input = int(input("Enter your age:"))
# check_age(input)


# def count_even(num):
#     count = 0
    
#     for n in num:
#         if n %2 == 0:
#             count = count + 1
            
#     return count
   
# num = [10, 15, 22, 31, 40, 51, 68]

# print("The total even numbers are:",count_even(num))

# def total_even(num):
#     total = 0
    
#     for n in num:
#         if n %2 == 0:
#             total = total + n
            
#     return total
    
# num = [10, 15, 22, 31, 40, 51, 68]

# print("The total numbers are",total_even(num))


# def find_highest(numbers):
    
#     highest = numbers[0]
#     for num in numbers:
#         if num > highest:
#             highest = num
            
#     return highest

# numbers = [45, 89, 23, 100, 67, 92]

# print("The highest number is",find_highest(numbers))


def find_lowest(numbers):
    
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
            
    return lowest

numbers = [45, 89, 23, 100, 67, 92]

print("The lowest number is",find_lowest(numbers))

   
        
    
