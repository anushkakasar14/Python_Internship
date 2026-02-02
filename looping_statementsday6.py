#Looping Statements:-iterating/looping/repeating

# executes same code ,multiple times until it becomes false..


#******************************
#while :-
#  syntax=
     #variable
        #while condition:
              #code to be executed
              
              
#example1:-
a=1
while a<=10:
    print("Hello welcome to python .......") 
    a+=1  #assignment operator
    
#example2:- print numbers from 1 to 100
b=1
while b<=100:
    print(b)
    b+=1
    
#example3:-even numbers between 1 to 100
c=2
while c<=100:
    print(c)
    c+=2
        
#example4:- even numbers between 1 to 100
d=1
while d<=100:
    if d%2==0:
        print(d)
    d+=1

#example5:-sum of even numbers between 1 to 50
e=1
sum=0
while e<=50:
    if e%2==0:
        sum=sum+e
    e+=1
print("sum of even numbers between 1 to 50 is:",sum)




#*************************************
#for in:-

#range() function:- it is used to generate a sequence of numbers.
#range(start,stop,step)

#for i in range(2,50):
 #   print(i)
                
#for j in range(2,51,2):
#    print(j)

#list=[10,20,30,40,50]
#for x in list:
#    print(x)

#for x in range(2,50,2):
 #   print(x)
 #   sum += x
#print("sum of even numbers between 1 to 50 is:",sum)

#*************************************************
#Break statement:-stops execution of program.
#it is used to terminatethe loop statement.
#example:-
for i in range(2,40):
    if i==4:
        break
    print(i)  #prints 2,3 and loop terminates when i=4
    
#************************************************
#Continue statement:-skips the current iteration and continues with next iteration.
#
#example:-
for i in range(1,10):
    if i==4:
        continue
    print(i)  #prints 1,2,3,5,6,7,8,9 (skips 4)
    
    
    
#************************************************
#nested for loop:-

for i in range(1,5): #outer loop
    print(i,"\n")
    for j in range(1,10): #inner loop
        print(j)
        
print("\n")     
   
#example:- print 5 table
no=5
for x in range(1,11):
    print(no*x)
    
 #example:- print multiplication table of given number
no=int(input("Enter a number:"))
for x in range(1,11):
    print(no*x)