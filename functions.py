#FUNCTIONS

# def welcome(name,age,usn):
#     print("Welcome to python")
#     print(name)
#     print(age)
#     print(usn)
    
# welcome("Likith",20,"4AL24CS114")



#FINDING SQUARE USING FUNCTION

# def square(number):
#     result = number * number
#     return result
# a = square(7)
# print(a)


#FINDING CUBE USING FUNCTION


# def cube(number):
#     result = number * number * number
#     return result

# ans = cube(8)
# print(ans)


#MULTIPLICATION USING FUNCTIONS


# def multiply(a,b):
#     result = a * b
#     return result

# ans = multiply(5,6)
# print(ans)


# CHECH EVEN OR ODD


# def check_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"
    
# ans = check_even(1)
# print(ans)


#FINDING EVEN IN LIST USING LOOPS


# def count_even(numbers):
#     count = 0
#     for num in numbers:
#         if num %2 == 0:
#              count = count + 1
#     return count
       
            
# numbers = [10, 15, 22, 31, 40, 51, 68]

# ans = count_even(numbers)

# print(ans)



#ADDING A EVEN NUMBERS IN THE LIST USING FUNCTION AND LOOPS


# def total_even(numbers):
#     total = 0
#     for num in numbers:
#         if num %2 == 0:
#             total = total + num
#     return total


# number = [10, 15, 22, 31, 40, 51, 68]

# ans = total_even(number)

# print(ans)


#FINDING HIGHEST NUMBER IN LIST USING FUNCTION AND 


# def find_highest(numbers):
#     highist = numbers[0]
#     for num in numbers:
#         if num > highist:
#             highist = num
#     return highist

# numbers = [45, 89, 23, 100, 67, 92]

# ans = find_highest(numbers)

# print(ans)



#FINDING THE HIGHEST AND LOWEST IN LIST


# def analyze(numbers):
#     highest = numbers[0]
#     lowest = numbers[0]
#     for num in numbers:
#         if num > highest:
#             highest = num
#         elif num < lowest:
#             lowest = num
#     return highest,lowest

# numbers = [45, 12, 67, 23, 89, 34]

# high,low = analyze(numbers)
# print(high,low)


#DEFAULT PATAMETER USING FUNCTION


def power(number, exponent=2):
    return number ** exponent

print(power(6))
print(power(2,3))

    


