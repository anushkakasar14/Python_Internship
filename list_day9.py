#************LIST IN PYTHON(Arrays)***************
#Is collection of similar or different data types of elements.
#stores in[]
#starts indexing from 0
# we can store multiple type of data in single variable.
#list are one of the most powerful and flexible data type in python.

#int a=20
#string a=""or''
#boolean=true|false
#none
#float a=25.3

#why list?-
#non primitive data type
#list hold str,int,float,boolean,none
#mutable-you can add,remove and update elements.
#to access ,modify and organize data efficiently
#commonly used in loops ,data storage and iteration.
list=[100,25.3,True,None,"Anushka"]
print(list)
skills=["html","js","tailwind","react","mongoDB"]
print (skills)


#####ACCESS LIST ELEMENTS-INDEXING {STARTS FROM(0)}
print(skills[0])
print(skills[1])

####### NEGATIVE INDEX(-1) STARTS FORM END 
print(skills[-1]) #mongoDB last value

#print(skills [10]) #error (list index out of range)



#**********TO CHECK LENGTH OF LIST
print(len(skills))



#****************************************
##WE CAN UPDATE GIVEN LIST:-
roles=["admin","manager","user"]
#update list element using index
roles[2]="super-admin"
print(roles)



#***********add elements to END of list************
#*******append()*********
roles.append("HR")
print(roles)


#**********ADD element on specific index*********
#####insert(index,value)***
roles.insert(0,"Developer")
roles.insert(1,"Developer")
print(roles)


#**********EXTEND()-use to merge or concatenate 2 or more lists****
#modify original list
list_1=["100","200",500,"om","vaibhav","aditya"]
list_2=[True,False,"Abc","xyz"]
 
#*******without extend******
##for x in list_2:
   # list_1.append(x)
    
#2
#print(list_1+list_2)

#3
#print(list_1,list_2)


####with append

list_1.extend(list_2)
print(list_1)
#print(list_1)
    
    
#*********POP()-use to remove elements from lists
#pop()-by default it will remove last element
#pop(index)-now it will remove specific element

list_3=[10,20,30,40,50,60,70]
list_3.pop() #10,20,30,40,50,60
list_3.pop() #10,20,30,40,50

list_3.pop(2)#10,20,40,50
print(list_3)


#******************************
##REVERSE-reverse list
list_3.reverse()
print(list_3)



#SORT-it sorts the list elements alphabatically or numerically

fruits=["apple","banana","cherry","pomegrante","grapes","orange","pineapple","custard apple","watermelon"]
fruits.sort()
print(fruits)

no=[100,200,520,45,22,222]
no.sort()###ascending order
no.reverse()#decending order
print(no)




####CLEAR-empty list

list_4=[10,40,50,80]
#list_4=[] 
 # or
list_4.clear()
print(list_4)


#**********REMOVE()************
#remove 1st matching elements

list_5=["html","css","nextjs","redux","mui","css"]
list_5.remove("css")
print(list_5)



#****************************
# copy-most IMP ******

#user=["pratik","bhavesh","shubham","aniket","aditya"]
#roles=["mernstack","python dev","ai engineer","sde-1","L-1"]

#assign roles in new_roles

#new_roles=roles
#new_roles.append("senior product manager")
#print(roles)
#print(new_roles)

#problem
#it has changes both lists
#to avoid this make indipendent copy of new list so it will not affect on original list
#solution-copy()
#create independent copy

roles=["mernstack","python dev","ai engineer","sde-1","L-1"]

###SHALLOW COPY 
new_roles=roles.copy()
new_roles.append("vice president")
print(roles)
print(new_roles)


# SEARCHING IN LIST
emp=["pratik","sanmesh","aditya","om","snehit"]

##membership operator-in and not in
print("pratik"in emp)
print("abc"in emp)
print("abc" not in emp)

#**********************************
#LOOPING-
for x in emp:
    print(x)


#************************
#Count**********
print(emp.count("pratik"))


#BUILT IN FUNCTION 
#len()
#min()
#max()
#sum()


list_6=[10,40,50,80,90,300,30]
print (max(list_6))  #300
print(min(list_6)) #10
print(sum(list_6))#600
print(len(list_6))


#*************************************************
##########slicing-extract some part of a list
#small part of data

#syntax:[start:end] ignore last

print(list_6[1:3]) #[40,50]
print(list_6[0:5]) #[10, 40, 50, 80, 90]
print(list_6[2])   #50
print(list_6[2:])   #[50, 80, 90, 300, 30]
print(list_6[:4])   #[10, 40, 50, 80]
print(list_6[:])     #[10, 40, 50, 80, 90, 300, 30]