#***********SETS IN PYTHON****************

#set is a collection of similar or different type of elements.
#unordered(no indexing or popsition)
#no duplicates allowed i.e, it removes duplicate values automatically.
# mutable (you can add or remove)
#uses curly bracket{}
# it dosent maintain order

# why sets?
#use to store unique values .
# used in mathematical operations like union,intersectins,to find difference.


sets={"omkar","aditya","pratik","nishant","snehit"}
print(type(sets))
print(sets)


#******************************************8
#*********empty sets**********

#sets_1={"ABC"}
#sets_1={}  //creates dictionary
sets_1=set()   #//empty set
print(sets_1)
print(type(sets_1))


###************************************
###union and intersection and difference
movie_1={"Dhurandhar","Saiyarra","Dhadak2","Sairat","Marco","Pushpa 2","KGF"}
movie_2={"Zindagi Na Milegi Dobara","Mission Impossible","Saiyarra","Tere Ishq me"}


print(movie_1)
print(movie_2)

#union :- itreturns combination of both sets
print(movie_1|movie_2)
 # OR
print(movie_1.union(movie_2))


#intersection:-it returns a common data from both the sets
print(movie_1&movie_2)
# OR
print(movie_1.intersection(movie_2))


#difference:-it returns a  items in A set but not in B set.
print(movie_1-movie_2)
# OR
print(movie_1.difference(movie_2))

print(movie_2-movie_1)
 # OR
print(movie_2.difference(movie_1))

#************************************
#pop():- remove
#add():- add single element
#update():-add multiple elements


emp={"anushka","alisha","srushti","samduddhi","sakshi"}
print(emp)
emp.add("saee")  #//to add single element
print(emp)

#//multiple elements
emp.update(["jaya","riya","tiya"]) 
print(emp)

#//removes random element
emp.pop() 
print(emp)

#//remove():- Remove specific element

emp.remove("anushka")
#emp.discard("disha") #remove value if found othewise code will run no errord occur
print(emp)

#//clear
emp.clear()
print(emp)


#*****************************************
##SETS FUNCTIONS*********************
no={10,20,80,40,50,60,70}
print(len(no))  #len()
print(max(no))  #max()
print(min(no))  #min()
print(sum(no))  #sum()
print(sorted(no))  #sorted()

#copy


#frozen set:-set that cannot be changed (like tuples for sets).

user=frozenset(["john","doe","mark","sundar","mac"])
#user.add("ABVC")
print(user)
