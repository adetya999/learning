
num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))
operator=input("Enter the operator + -  * / ")
if operator=="+":
    result=num1+num2
    print(f"The sum is {result}")
elif operator=="-":
    result =num1-num2
    print(f"The diff is {result}")
elif operator=="*":
    result=num1*num2
    print(f"The product is {result}")
elif operator=="/":
    result=num1/num2
    print(f"The sum is {result}")
else:
    print(f"invalid operator!!!")
    
    