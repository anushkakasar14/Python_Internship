#***************Exception Handling*****************

#exception is an error that stops your program while running.


#def Calci(a,b):
 #   return a/b
#print(Calci(5,5))

#res=Calci(50,0)
#print(res)

#def demo():
   # print(a+"cvb")
 #  print(a+b)
#demo(100,200)
#next
##def user():
   # print("user function")
#user()

#print("hello welcome dear")

#Examples:-
#_dividing by zero
#accessing undefined variable
#wrong input from user
#opening a file that doesn't exist

 #*****WHY USE EXCEPTION HANDLING?**********
 # prevent program crash
 #handle wrong user inputs
 #continue execution even after error
 # make program more professional
 
 
 #Try-Except Basic Syntax:-
try:
    a=20
    b="anushka"
    print(a+b)
except Exception as err:
    print("Error Occured ",err)

print("hello anushka ")
 
 
#Example:-

try:
    def Calci(a,b):
        return a/b
    print(Calci(5,5))
    
    res=Calci(50,0)
    print(res)
except Exception as err:
    print("Error occured.....",err )
    
print("hello world")


#**************************************************
try:
    x=100
    y="300"
    print(x+y)
except ValueError:
    print("error occured")
except ZeroDivisionError:
    print("error occured")
except TypeError:
    print("error occured")
    
    
    
    
    #***************************************
#eg:
try:
    x=100
    y="50"
    print(x+y)
except Exception as error:
    print("error occured",error)
finally:
    print("code executed successfully")   #// always runs (cleanup code)
    

#*****************************************************
#Raising  Your Own Errors
try:
    age=int(input("Enter Your Age...."))
    def demo(a):
        if  a<=0:
            raise ValueError("Age Cannot be negative")
        print("Your Age is :",a)
    demo(age)
except Exception as e:
    print("Error",e)
    
