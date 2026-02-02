
#****************FUNCTION:-********************
#function is block of code that runs when its called.
#code reusability,irganize code,avoid repetition
#mini program inside your program
#define once and use multiple time

#syntax:-
#def function-name()     #function declaration/defination
    #block of code
#function-name()      #function call
    

#example
def demo():
    print("hello function")
demo() 

def greet():
    print("welcome to our program")
greet()

#************

def add():
    print(20+40)
add()
add()
add()


#***********************************************
#**********PARAMETERS AND ARGUMENTS*******************
#to pass dynamic values inside function

##PARAMETET:-values which we pass during function declaration /defination

#ARGUMENTS:-actual valus which we pass while function calling.

def sum(a,b):
    print (a+b)
sum(30,40) #70

    #*****************************************
def checkEligibility(age):
    if (age>=18):
        print("congrats.....")
    else:
        print("sorry.....")
userAge=int(input("enter your age...."))

checkEligibility(userAge)
#*******************

def UserInfo(userName,userSkills,userAddress):
    print(f"your nameis{userName},your skill is{userSkills},your address is{userAddress}")

UserInfo("om","python","pune")
UserInfo("Anushka","SQL","pune")


def evenOdd(no):
    result="Even no"if no%2==0 else "Odd no"
    print(result)
    
evenOdd(20)
evenOdd(30)





#****************************************************
#*******************RETURN KEYWORD*******************
#use to return values outside the function itself
#it stops the execution of our program after returning 

def mult(x,y):
   #print(x*y)
    return x*y

res=mult(10,20)#itself have that value
print(res)




#example:
def demo(name,skills):
    print(name+""+skills)
    return name+skills
    print("hello world") # code written after return is not executable
demo("sanmesh","React")



def add(a,b,c):
    print(a+b+c)
add(5,10,20)
#add(50,20)
#add(20)
#add(50,60,22,11)
 