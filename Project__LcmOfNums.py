a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

max_num = max(a,b)
while(True):
    if(max_num%a == 0 and max_num%b == 0):
        break
    max_num = max_num+1

print("the Lcm out of  ",a,"and ",b,"is :",max_num)