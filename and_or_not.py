#AND operation

# age = 20
# has_id = True

# if age >= 18 and has_id:
#     print("You are eligible")
# else:
#     print("You are not eligible")


#OR operation

# day = "Sunday"

# if day == "Sunday" or day == "Saturday":
#     print("Weekend")
# else:
#     print("Weekday")

#NOT operation

# is_raining = False

# if not is_raining:
#     print("Go outside")
# else:
#     print("don't go outside")


#Login

# username = "admin"
# password = "python123"

# if username == "admin" and password == "python123":
#     print("You are logined")
# else:
#     print("Incorrect Password or Username")

#Scholarship

# percentage = 88
# attendance = 80

# if percentage >= 85 and attendance >= 75:
#     print("Scholorship Granted")
# else:
#     print("Not Granted")


#Discount

# amount = 3000
# is_member = True

# if amount >= 5000 or is_member == True:
#     print("You got discount")
    
# else:
#     print("Can't get discount")


#Security Check

# logged_in = True
# banned = False

# if logged_in == True and banned == False:
#     print("You are logined")
# else:
#     print("Not logined")


#Predict the Output

# a = 10
# b = 20

# print(a > 5 and b > 15)
# print(a > 15 and b > 15)
# print(a > 15 or b > 15)
# print(not(a > 15))


#Predict the Output


# age = 20
# has_id = True
# banned = False

# result = age >= 18 and has_id and not banned

# print(result)


#AI/ML-style Problem

# accuracy = 92
# precision = 89

# if accuracy >= 90 and precision >= 80:
#     print("Model redy")
# else:
#     print("Model not redy")


#Entry System

# age = 20
# has_id = True

# if age >= 18:
#     if  has_id == True:
#         print("You are eligible")
#     else:
#         print("Not eligible")
# else:
#     print("Underage")
    

#Login + OTP

# username = "admin"
# password = "python123"
# otp = 1234

# if username == "admin" and password == "python123":
#     print("You are logined")
#     if otp == 1234:
#         print("logined")
#     else:
#         print("Incorrect otp")
# else:
#     print("Incorrect Password or username")


#Exam Eligibility

# attendance = 80
# fees_paid = True

# if attendance >= 75:
#     if fees_paid:
#         print("Eligible for exam")
#     else:
#         print("Fees did't paied")
# else:
#     print("Not Eligible for exam")

#Driving License

# age = 20
# has_learning_license = True

# if age > 18:
#     if has_learning_license:
#         print("You can Drive")
#     else:
#         print("You can't Drive")
# else:
#     print("You are not eligible for driving")


#ATM

# balance = 10000
# withdraw = 7000
# pin_correct = True

# if pin_correct:
#     if withdraw == 7000 and withdraw > 0:
#         if balance == 10000:
#             print("You can withdraw money")
#         else:
#             print("Incufficent Balance")
#     else:
#         print("Incufficent Balance or Enter correct amount")
# else:
#     print("Enter the correct Pin")


#College Admission

# percentage = 82
# entrance_exam = True

# if percentage > 80:
#     if entrance_exam:
#         print("You can Selected")
#     else:
#         print("You are not Selected")
# else:
#     print("You are not eligible")

#Bank Loan

# age = 30
# salary = 50000
# credit_score = 750

# if age > 21:
#     if salary > 30000:
#         if credit_score > 500:
#             print("You can Apply")
#         else:
#             print("Your credit score is low")
#     else: 
#         print("You don't have sufficent salary")
# else:
#     print("You are Minor")

#AI Model Deployment

# accuracy = int(input("Enter the Accuracy:"))
# precision = int(input("Enter the Precision:"))
# model_tested = bool(input("Enter the Model Test:"))

# if accuracy >= 90:
#     if precision >= 85:
#         if model_tested:
#             print("The model is tested")
#         else:
#             print("The model is not tested")    
#     else:
#         print("Precision is low")
# else:
#     print("accuracy is low")