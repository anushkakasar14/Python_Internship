
####CONTROL STATEMENTS IN PYTHON####
#controlling the statements-Decision making power


#conditional statements-check condition(trur/false) and execute code accordingly
#ternary operator-"output if true" if condition else "output if false"
#syntax: value_if_true if condition else value_if_false

#*******************************************
# if-:check 1 conditon at a time
# syntax:if(condition)

#example1:


number=int(input("Enter a number to check given no is even or odd:"))
if(number%2==0):
    print("even number=",number)
if(number%2!=0):
    print(" odd number=",number)
    
    
#example2:
age=int(input("Enter your age:"))
if(age>=18):
    print("You are eligible to vote")
if(age<18):
    print("sorry not eligible to vote")


#example3:
shopping_amount=int(input("Enter the shopping amount:"))
discount=0
if(shopping_amount>=10000):
    discount=10
    
if(shopping_amount<10000):
    discount=0
  

discount_amount=shopping_amount*discount/100

net_total=shopping_amount-discount_amount

print(f"Your Shopping Amount Is: {shopping_amount}")
print(f"Your Discount Is: {discount}%")
print(f"Your Discount Amount Is: {discount_amount}")
print(f"Your Net Total Is: {net_total}")
    
print("Thank you for shopping with us")

#*******************************************

# if else:-check 1 condition and provide alternative action if condition is false
#syntax:if(condition):
#          block of code
#       else:
#          block of code

#example1:
if(True):
    print("Hello World")
else:
    print("Hello Universe")   
    
#example2:
age=int(input("Enter your age:"))
if(age>=18):
    print("You are eligible to vote")       
else:
    print("sorry not eligible to vote")
    
#example3:
no=int(input("Enter a number to check given no is even or odd:"))
if(no%2==0):
    print("even number=",no) 
else:
    print(" odd number=",no)  
    
    
#example4:
score1=int(input("Enter your score1:"))
score2=int(input("Enter your score2:"))
score3=int(input("Enter your score3:"))
score4=int(input("Enter your score4:"))
score5=int(input("Enter your score5:"))
score6=int(input("Enter your score6:"))

if(score1>=35 and score2>=35 and score3>=35 and score4>=35 and score5>=35 and score6>=35): #all subjects pass condition/all conditons true
    print("You are passed in the exam")

    percentage=((score1+score2+score3+score4+score5+score6)/600)*100
    print("Your percentage is:",percentage)
    
    if(percentage>=75):
        print("You got Distinction",percentage)
    else:
       
        print("You got First Class",percentage)
        
        
else:
    print("You are failed in the exam")

#*******************************************


# if elif else:-check multiple conditions at a same time
#syntax:if(condition1):
#          block of code
#       elif(condition2):
#          block of code
#       else:
#          block of code

#example1:
a=int(input("Enter first number a:"))
b=int(input("Enter second number b:"))
c=int(input("Enter third number c:"))

if(a>b and a>c):
    print("a is the largest number:",a)
elif(b>a and b>c):
    print("b is the largest number:",b)
else:
    print("c is the largest number:",c)
    
    
   
#example:
shopping_amount=int(input("Enter the shopping amount:"))
discount=0
if(shopping_amount>=10000 and shopping_amount<20000):
    discount=20
elif(shopping_amount>=20000 and shopping_amount<30000):
    discount=30
elif(shopping_amount>=30000 and shopping_amount<40000):
    discount=40
elif(shopping_amount>=40000 and shopping_amount<50000):
    discount=50
else:
    discount=0
    
discount_amount=shopping_amount*discount/100
net_total=shopping_amount-discount_amount
print(f"Your Shopping Amount Is: {shopping_amount}")
print(f"Your Discount Is: {discount}%")
print(f"Your Discount Amount Is: {discount_amount}")
print(f"Your Net Total Is: {net_total}")
print("Thank you for shopping with us")


#*******************************************


#match case( python 3.10 and above):-

#-used to handle multiple cases at a same time
#-handle multiple opearartions at same time

#syntax:
# 
# match variable:
#          case1:
#              block of code
#          case2:
#              block of code
#          case3:
#              block of code
#          case _:
#              block of code


#example1:
day=int(input("Enter a day number:"))
match day:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _: #default case
        print("Invalid day number")



#Example2:Calculator using match case

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

operator=input("Enter an operator: + , - , * , / ")
match operator:
    case "+":
        print("Addition is:",{num1+num2})
    case "-":
        print(f"Subtractions is:{num1}-{num2}={num1-num2}")
    case "*":
        print(f"Multiplication is:{num1}*{num2}={num1*num2}")
   
    case "/":
        if(num2!=0):
            print(f"Division is:{num1}/{num2}={num1/num2}")
        else:
            print("Error: Division by zero is not allowed")
    case _:
        print("Invalid operator")   
        
        
#example3:
day=(input("Enter a day:"))
match day():

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
    
        print("It's a Weekday")
    case "Saturday"| "Sunday": #Bitwise operator used
        
        print("It's a Weekend")
    case _:
        print("Invalid day")
        
        
#*****************************************

#Looping statements-repeating a block of code multiple times
 
#for in loop,

#while loop,




#************************************************
