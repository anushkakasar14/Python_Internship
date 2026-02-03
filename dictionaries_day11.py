#***Dictionary*******

#dictionar/object
#dictionary in Python is used to store data in key-value pair.
#Ordered (from Python 3.7+)
#Mutable (can change values)
#No duplicate keys allowed [all keys must be unique]
#Keys must be unique and immutable (like strings, numbers, tuples)
#Values can be any data type
# have methods and properties


########WHY USE DICTIONARY?
#-to store related data (like an object or record)
#-to quickly find a value using a key
#-to represent real worls dta like users,products,students,etc.
#-access data via name indexing.
  
#syntax:
#dictionary_name:{
#    "key1":"value1",
#    "key2":"value2"
# }



#example:
student={
    "name":"anushka",
    "age":"21",
    "city":"nagar"
}
print(student)

#example2:
car={
    "brand":"TATA",
    "model":"sieara",
    "year":2026
}
print(car)

##accessing values 
print(car["brand"])
print(car["model"])
print(car["year"])

#Using get() avoids an error if the key doesn’t exist it result none
print(car.get("engine")) #none


#***********************************
#****Changing Values***


#You can UPDATE the value of a specific key.
car["year"]=2025
print(car)

car["brand"]="Toyota"
print(car)

car["model"]="fortuner"
print(car)

#*********************************
######ADDING new key-value pair**
car["color"]="RED"
print(car)

car["acceseries"]="speakers","interior"
print(car)


#************************************
#looping:-

#for in

# it will return keys
for x in car:
    print(x)
    
    
# keys
for x in car.keys():
    print(x)
    
    
#values:-it returns values from dictionary
for x in car.values():
    print(x)
    
    
#items:-it returns both key an value pair 
for x in car.items():
    print(x)
    
#************************************************
#MEMBERSHIP OPERATOR:-in and not in

#check exist or not
res="brand" in car
print(res)

res="color" in car
print(res)





#len
print(len(car))

#type
print(type(car))

#clear
car.clear()
print(car)

#copy
dict1={
    "user":"anushka",
    "email":"anush@gmail.com"

}

dict2={
    "address":"ahilyanagar",
    "skill":"python"
    
}
#dict3=dict2
##dict2["skill"]="Ai engineer"
#dict2["role"]="software developer"


#copy method
dict3=dict2.copy()
dict2["skill"]="Ai engineer"
print(dict1)
print(dict2)
print(dict3)


#update-update one dictionary with another

products={
    "ProductName":"Mac",
    "ProductPrice":"1lac",
    "ProductDetails":{
        "ram":"16GB",
        "rom":"256GB",
        "processor":"m4"
        }
}
products.update({"productofferprice":"8000","productbrand":"Apple"})
print(products)



#*********************************
#pop:-use to remove data
#must pass key name

products.pop("ProductDetails")

print(products)


####*****************************************8
#list to tuple
list3=["mahesh","sanket","om","aditya"]
print(list3)
print(tuple(list3))


##dict
#list of tuples
list4=[("age","address"),(21,"nagar")]
print(list4)
print(dict(list4))

#*************************************8
#setDefault -use to set default values
#if key is present then it will consider existing one else default one
student={
    "name":"om",
    "address":"nagar",
   # "role":"mern developer"
}
student.setdefault("role","software trainee") #setDefault
print(student)
