#CALCULATOR

print("WELCOME TO THE CALCULATOR")
a=int(input("ENTER 1st number "))
print("PRESS + FOR ADDITION")
print("PRESS - FOR SUBTRACTION")
print("PRESS * FOR MULTIPLICATION")
print("PRESS / FOR DIVISION")
cd=input("ENTER YOUR OPERATOR ")
b=int(input("ENTER 2nd NUMBER "))
if cd=="+":
    s=(a+b)
    print("THE SUM OF 2 NUMBERS IS",s)
elif cd=="-":
    s=(a-b)
    print("THE SUBTRACTED VALUE IS",s)
elif cd=="*":
    s=(a*b)
    print("THE PRODUCT OF 2 NUMBERS IS",s)
elif cd=="/":
    s=(a/b)
    print("THE DIVIDED NUMBER IS",s)
else:
    print("ENTER A VALID CONDITION")

print("PRESS 1 to ADD : 2 to SUBTRACT : 3 to MULTIPLY : 4 to DIVIDE : 5 to EXIT")
while True:
    operation=int(input("ENTER YOUR CHOICE "))
    if operation==1:
        n=int(input("ENTER THE NUMBER "))
        s=(s+n)
        print("THE NEW NUMBER IS ",s)
    elif operation == 2:
        n=int(input("ENTER THE NUMBER "))
        s=(s-n)
        print("THE NEW NUMBER IS ",s)
    elif operation == 3:
        n=int(input("ENTER THE NUMBER "))
        s=(s*n)
        print("THE NEW NUMBER IS ",s)
    elif operation == 4:
        n=int(input("ENTER THE NUMBER "))
        s=(s/n)
        print("THE NEW NUMBER IS ",s)
    elif operation == 5:
         print ("CLOSING THE PROGRAM")
         print("THANK YOU")
         break
    
    else:
         print("INVALID CHOICE")