print("hello welcome to python \n. hello dear \t hello")



#Type Casting =convert one data type into another


age=int("20")

print(age)
print (type(age))


 #str()
 #float()
 #bool()
 
 
a=20
b="30"
 
print(a +int( b))


#Example

empId= str(1234)
print(empId)

print(type(empId))


#***********
# String Concatination

#   +
#   ,
#   f"" modern and easy -recommended

name="Aditya"
skill="Python"

print("Your name is ",name)
print(f'Your name is (name)')
print("Your name is "+name)




#*****************
#can use addion operator only with same data types

#number1=100
#number2=23
#print(number1+number2)


#number1=100
#number2="23"
#print(type(number1))
#print(type(number2))
#print(number1+number2)    ####error


number1=100
number2=int(23)
print(type(number1))
print(type(number2))
print(number1+number2)


#  , most useful for merging or concat

#autonamtically convert into string

no1=230
no2="20"
print(no1,no2)



empRole="Developer"
empAddr="Pune"

print("Your role is "+empRole+" and your address is "+empAddr)
print("Your role is ",empRole," and your address is ",empAddr)


#########

# F-String = modern and easy way to concat strings and variables

empAge=30
ampCTC="20 lpa"

print(f"Your age is {empAge} and your CTC is {ampCTC}")


#Summary:

# Identifiers =Unique name to identify that variable. / Names we use for variables, functions, classes, etc.
# + : used to concat strings only of same data types (need conversion)
# , : used to concat strings of different data types (auto conversion)
# f"" : modern and easy way to concat strings and variables



#####  TASK  #####
age="20"
name="sanmesh"
skill="python"
role="developer"

print("your name is "+name+" your age is "+age+" your skill is "+skill+" your role is "+role)
print("your name is ",name,"your age is",age,"your skills is",skill,"your role is",role)
print(f"your name is {name} your age is {age} your skill is {skill} your role is {role}")



#***************************************

##  Take input from user
# input() :function is used to take input from user
# By default returns string data 

#name="pratik"
name=input("Enter your name: ")
print("your name is",name)


#*****************

no1=input("Enter no1: ")
no2=input("Enter no2: ")

print("sum is: ",(no1+no2)) 
# by default all inputs are string data types

# if we want to perform arithmetic operation we need to convert into int or float

no1=int(input("Enter no1: "))
no2=int(input("Enter no2: "))
print("sum is: ",(no1+no2))




#********************************

# Python Reserve Words/Keywords

# these words are reserved by python and having some special meaning
# we cannot use these words as identifiers/variable names

#true
#false
#if
#input
#type
#int
#print
#for




import keyword
print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#*************************
#id - used to get the memory address of variable


x=10
print(id(x))
print(x)

y=20
print(id(y))
print(y)



x=200
print(id(x))
print(x)