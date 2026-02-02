#*************Operators in python**************

# 1. Arithmetic operators: +, -, *, /, %, //, ** 

## a+b=
# a,b= operands
# +,-,*,/,%= operators
# expression: combination of operands and operators



a=100
b=20
print(a+b) #120
print(a*b) #2000
print(a-b) #80
print(a/b) #5
print(a%b)  #0

print(2**3) # returns power 2^3=8
print(5**3) # returns power 5^3=125


#BODMaS Rule
#higher priority: Brackets, Orders (i.e. powers and square roots, etc.), Division and Multiplication, Addition and Subtraction
#lower priority: Addition and Subtraction


print(a*b+a) #2000+100=2100
print(a+b/a) #b/a=20/100=0.2+100=100.2
print(a*b/a) #2000/100=20.0
print(a+(b*a)) #20*100=2000+100=2100

#********************************
#*2. Comparison operators: use to compare two values and return boolean value True or False
# ==(equal to equalto), !=(not equal), >, <, >=, <=

x=20
y=30
print(x==y) #False
print(x!=y) #True
print(x>y)  #False
print(x<y)  #True
print(x>=y) #False
print(x<=y) #True


print(20!=20) #False
print(20=="20") #False



#********************************

#*3. Logical operators: and, or, not
#use to handle conditional statements at same time

# and operator: returns True if both statements are true
# or operator: returns True if one of the statements is true
# not operator: reverse the result, returns False if the result is true

##1=True
#0=False 
#and operator                         
#1 and 1 =1
#1 and 0 =0
#0 and 0 =0
#0 and 1 =0


P=200
R=500
Q=300

print(P>=R and P<=R) #False


#OR operator - returns True if one of the statements is true
#1 or 1 = 1
#1 or 0 = 1
#0 or 0 = 0
#0 or 1 = 1
print(P<=Q or Q<=R) # True||True= True



#NOT operator - reverse the result
print(not(10<2)) #True
print(not(10>2)) #False



#********************************
#*4. Assignment operators: used to assign values to variables
# =, +=, -=, *=, /=, %=, //=, **=
#LHS=RHS

a=20
b=a
print(b,a) #20 20

no1=20
no2=40

print(no1+no2) #60
no1+=no2 # no1=no1+no2
print(no1) #60
print(no2) #40

no1*=no2 # no1=no1*no2
print(no1)  # 60*40=2400
print(no2)  #40


no2-=no1 # no2=no2-no1 =40-2400=-2360
print(no1)  #2400
print(no2)  #-2360


#*****************************
#*5. Bitwise operators: works on bits and performs bit by bit operation
# &, |, ^, ~, <<, >>
#AND, OR, XOR, NOT, left shift, right shift

#convert decimal to binary 

print(5&3) #1 
 
 # 5:
 # 8 4 2 1      rules for binary
 # 0 1 0 1
 
# 3:
## 8 4 2 1
 # 0 0 1 1
   
 
print(5&8) #0

#5=0101
#8=1000
  # 0000=0
   
   
   
###############################
# 6.Ternary operator: used to evaluate something based on a condition being true or false
 # syntax: value_if_true if condition else value_if_false
 
 
 
age=int(input("Enter your age: "))
result="Congrats bro"  if age>=18 else "Sorry bro, wait some time"
print(result)


#Example:
year=int(input("Enter your year: "))
result="Gen Z"  if year>=2000 else "Millennial"
print(result)



#*******************************************
# 7.Membership Operators**************
# in, not in
#used to check whether element is present or not.


print ("membership operators in python")

data=[20,40,60,100,30,"OM","aditya",True,None,23.5]
print("OM"in data)  #True
print("ABC" not in data)   #True
print(100 in data)  #True




#*******************************************
# 8.Identity Operators**************  
# is, is not
#used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

a=[1,2,3]
b=a
c=[10,20,30]
print(a is b)  #True
print(a is c)  #False
print(a is not b)  #False