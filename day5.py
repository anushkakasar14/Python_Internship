# CONSTANT VALUES
 #use capital letters when you want to define constant values.
# Its just a convention - we use uppercase letters to indicate that these values-i.e we can change these values .

EMP_ID=100152255
skill="Python"
role="Developer"
ctc="12 LPA"

print(f"""
      
   EMP_ID : {EMP_ID}
   skill  : {skill}     
   role   : {role}
   ctc    : {ctc}   
   
  """   )


########IMPORTANT_NOTE##########
name=input("Enter your name: ")
m1=int(input("Enter marks1: "))
m2=int(input("Enter marks2: "))
m3=int(input("Enter marks3: "))
m4=int(input("Enter marks4: "))

print(f"your name is {name} and your total marks is {m1+m2+m3+m4} and you got percentage {(m1+m2+m3+m4)/4}%")




# MEMORY MANAGEMENT IN PYTHON
x=40
y=x # y is pointing to same object as x in memory.
print(id(x)) 
print(id(y)) #  same id as x because both are pointing to same object in memory.


#*********Mutable vs Immutable objects in python*********

p=30
print(p) #30
print(id(p)) #140721142712136

p=50
print(p) #50
print(id(p))  #140721142712776
# new memory location because integers are immutable objects.

# Immutable objects- int, float, string, tuple (cannot be changed)(primitive data types are immutable)
# Mutable objects- list, dict, set (can be changed)





  