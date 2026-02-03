###########TUPLES IN PYTHON*************

# A Tuple is collection of ordered ,unchangeable(immutable) items in python.
# it is collection of similar or different types of elements.
#we caan store multiple types of data in a single variable.
#IMMUTABLE i.e, Fixed size length stored in memory like a pointer.
# Starts indexing from 0

#define using parentheses()
#store multiple values
# Immutable -cannot update,add or remove items once created
#  is faster than list because of its fix side length
#tuples takes less memory and are faster because they are immutable.

#1-syntax:
skill=("html","css","JS","Python")
print(skill)
print(skill[2])

#2-without ()
emp="HTML","CSS","JS"
print(type(emp))
print(emp)

#3-for single element
#emp=("pratik") # consider string by default
emp=("pratik",)
print(type(emp))
print(emp)



#******************************************************************
#*********LOOPING******************
user=("john","motu","patlu","shiva","aditya","singchan")
print(user)    
for x in user:
    print(x)
    
    
    
#***********slicing-extra data*******
print(user[1:6])
print(user[:3])
print(user[2:])




#**********range function- fetch data from 2-5
for x in range(2-6):
    print(user(x))
    
#*************************
    
for i in range (len(user)):
    print(user[i])
    
    
#********************************************************
########Built in function
#sum()
#len()
#min()
#max()

tuple_1=("AWS","NextJS","NestJS","Expressjs","nodejs")
print(tuple_1)
print(len(tuple_1))

tuple_2=(20,23,25,27,21)
print(min(tuple_2))
print(max(tuple_2))
print(sum(tuple_2))



#***************searching************************


#*****membersghip operator-in and not in****************
res="JS" in tuple_1
print(res)




#*********sorted************
print(sorted(tuple_2))



#**********count**********
print(tuple_1.count("AWS"))
print(tuple_2.count("AWS"))


#*****************************************


#************Packing and Unpacking***********

brands=("samsung","lenovo","Apple","Toshiba","Xiaomi","Realme")
print(brands)
print(brands[0])
print(brands[1])


####unpacking
#modern way
brand1,brand2,brand3,brand4,brand5,brand6=brands
print(brand1)
print(brand5)


#*****************************************
user=("om","pune","23")
#print(user[0])
#print(user[1])
name,city,age=user
print(name)
print(city)
print(age)




#############list to tuple
list_1=[10,30,40,50]
print(type(list_1))
print(list_1)

print(tuple(list_1))

#************tuple to list*********
tuple_2=(100,200,300,400)
print(type(tuple_2))
print(tuple_2)
print(list(tuple_2))

#******************************************
