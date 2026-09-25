a = int(input("Enter 1st number --> :"))
b = int(input("Enter 2nd number --> :"))

operators = input("enter operators (+ , - , % , /) :")

if(operators == "+"):
    result = a+b
elif(operators == "-"):
    result = a-b
elif(operators == "*"):
    result = a*b
elif(operators == "%"):
    result = a%b
elif(operators == "/"):
    if(a==0 and b==0):
        result = 0
    else:
        result = a/b
    
else:
    result = "unvalid operation"


print("The result is ---> :" , result)
