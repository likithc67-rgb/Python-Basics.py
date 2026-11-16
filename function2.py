'''Returning Multiple Values'''

# def calculate(numbers):
#     total = 0
    
    
#     for num in numbers:
#         total = total + num
#     average = total / len(numbers)
#     return total,average
  
# numbers = [10, 20, 30, 40, 50]



# total,avrage = calculate(numbers)

# print("total:",total)
# print("average:",avrage)


def analyze_marks(marks):
    total = 0
    highest = marks[0]
    lowest = marks[0]
    
    for num in marks:
        total = total + num
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num
    average = total / len(marks)
            
    return total,highest,lowest,average

marks = [78, 92, 45, 33, 87, 29, 95, 61]

total,highest,lowest,average = analyze_marks(marks)
print("Highest:",highest)
print("Lowest:",lowest)
print("Total:",total)
print("Average:",average)
    
    