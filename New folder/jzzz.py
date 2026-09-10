a = float(input("enter the 1st num: "))
b = float(input("enter the 2nd num: "))
op = input("enter operator (+,-,*,%,/): ")

if op =='+':
    print(a+b)
elif op =='-':
    print(a-b)
elif op =='*':
    print(a*b)
elif op =='%':
    print(a%b)
elif op =='/':
    print(a/b)
else:
    print("invalid operation")