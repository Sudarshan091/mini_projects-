#lets  take two number as input from the user 
Number1= int(input("Enter first number:"))
Number2= int(input("Enter your second number :"))
#perform some basic  operation on these two number 
choosing_operation = input("Enter the operation you want to do (+,-,*,/):")
if choosing_operation == "+":
    result = Number1+Number2
    print("the result is :", result)

elif choosing_operation == "-":
        result = Number1-Number2
        print("the result is :", result)

elif choosing_operation == "*":
    result= Number1*Number2
    print("the rsult is :", result)

elif choosing_operation == "/":
    result =Number1/Number2
    print("the result is :", result)         

else :
    print("Invalid operation selected")    

