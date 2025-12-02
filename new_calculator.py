num1=int(input("enter th first number:"))
num2=int(input("enter the second number:"))
choosing_operation=input("enter the operaton (+,-,/,*,%,**)")
if(choosing_operation=="+"):
    print("result is:", num1+num2)
elif(choosing_operation=="-"):
    print("result is:", num1-num2)
elif(choosing_operation=="/"):
    print("result is:", num1/num2)
elif(choosing_operation=="*"):
    print("result is:", num1*num2)
elif(choosing_operation=="%"):
    print("result is:", num1%num2)    
elif(choosing_operation=="**"):
    print("result is:", num1**num2)
else:
    print("invalid operation selected")    