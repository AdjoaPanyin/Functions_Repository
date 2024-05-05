def calculator():
    num1=float(input("enter first number \n"))
    operator= input("enter operator(+,-,/,*) \n")
    num2= float(input("enter second number \n"))

    if operator=='+':
        print(num1 + num2)
    elif operator =='-':
        print(num1 - num2)
    elif operator =='*':
        print(num1*num2)
    elif operator=='/':
        if num2 !=0:
            print(num1/num2)
        else:
            print("Zero division error")

calculator()